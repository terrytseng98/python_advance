let model,
    webcam,
    labelContainer,
    maxPredictions,
    position = -1,
    range,
    check = -1,
    lastrange = -1;
var target_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

async function init() {
    const URL = document.getElementById("modelin").value;
    const modelURL = URL + "model.json";
    const metadataURL = URL + "metadata.json";

    model = await tmImage.load(modelURL, metadataURL);
    maxPredictions = model.getTotalClasses();

    const flip = true;

    webcam = new tmImage.Webcam(640, 640, flip);

    await webcam.setup();
    await webcam.play();

    window.requestAnimationFrame(loop);

    document.getElementById("webcam-container").appendChild(webcam.canvas);

    for (let i = 0; i < maxPredictions; i++) {
        var tt = "myProgress" + (i + 1);
        var elem = document.getElementById(tt);
        elem.style.width = 200 + "pt";
    }
}

async function loop() {
    webcam.update();
    await predict();

    window.requestAnimationFrame(loop);
}

async function predict() {
    const prediction = await model.predict(webcam.canvas);
    for (let i = 0; i < maxPredictions; i++) {
        if (range < prediction[i].probability.toFixed(2)) {
            range = prediction[i].probability.toFixed(2);
            position = i;
            lastrange = range;
        }
        var elem = document.getElementById("myBar" + target_list[i]);
        elem.style.width = prediction[i].probability.toFixed(2) * 100 + "%";
        document.getElementById("myBar" + target_list[i]).innerHTML =
            (prediction[i].probability.toFixed(2) * 100).toFixed(0) + "%";
        document.getElementById("label" + target_list[i]).innerHTML =
            prediction[i].className;
    }
    if (lastrange > 0.7) {
        if (position != check) {
            try {
                publish(String(prediction[position].className));
                check = position;
            } catch (error) {
                // pass
            }
        }
    }
    range = -1;
}

// Called after form input is processed
function startConnect() {
    topic = document.getElementById("topic").value;

    // Initialize new Paho client connection
    client = mqtt.connect("ws://singularmakers.asuscomm.com:11883", {
        username: "singular",
        password: "1234",
    });

    client.on("connect", function () {
        client.publish(topic, "Hello!");
    });
}

// Updates #messages div to auto-scroll
function updateScroll() {
    var element = document.getElementById("messages");
    element.scrollTop = element.scrollHeight;
}

function publish(target) {
    topic = document.getElementById("topic").value;
    document.getElementById("messages").innerHTML +=
        "<span>topic:" + topic + ", publish:" + target + "</span><br/>";
    updateScroll();
    client.publish(topic, target);
}
