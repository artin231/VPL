function updateDashboard() {

    fetch("use_AI_for_physics/sim1/result", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            y0: document.getElementById("y0").value,
            speed: document.getElementById("speed").value,
            angle: document.getElementById("angle").value,
            resistance: document.getElementById("resistance").value,
            time: document.getElementById("time").value
        })
    })
    .then(res => res.json())
    .then(data => {

        const x = data.x;
        const signals = data.signals;
        const names = Object.keys(signals);

        Plotly.react("plot1", [{
            x: x,
            y: signals[names[0]],
            mode: "lines",
            name: names[0]
        }], { title: names[0] });

        Plotly.react("plot2", [{
            x: x,
            y: signals[names[1]],
            mode: "lines",
            name: names[1]
        }], { title: names[1] });

        Plotly.react("plot3", [{
            x: x,
            y: signals[names[2]],
            mode: "lines",
            name: names[2]
        }], { title: names[2] });

        Plotly.react("plot4", [{
            x: x,
            y: signals[names[3]],
            mode: "lines",
            name: names[3]
        }], { title: names[3] });

    });
}

updateDashboard();