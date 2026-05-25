

// let pieChart, barChart, areaChart;
// let historyData = [];
// let historyLabels = [];

// let alarmUnlocked = false;
// let alarmPlayed = false;

// function initCharts() {
//     const pieCtx = document.getElementById("pieChart").getContext("2d");
//     const barCtx = document.getElementById("barChart").getContext("2d");
//     const areaCtx = document.getElementById("areaChart").getContext("2d");

//     pieChart = new Chart(pieCtx, {
//         type: "pie",
//         data: {
//             labels: ["Safe", "Intermediate", "High Risk"],
//             datasets: [{
//                 data: [0, 0, 0]
//             }]
//         }
//     });

//     barChart = new Chart(barCtx, {
//         type: "bar",
//         data: {
//             labels: ["Male", "Female"],
//             datasets: [{
//                 label: "Count",
//                 data: [0, 0]
//             }]
//         }
//     });

//     areaChart = new Chart(areaCtx, {
//         type: "line",
//         data: {
//             labels: [],
//             datasets: [{
//                 label: "Crowd Count",
//                 data: [],
//                 fill: true,
//                 tension: 0.3
//             }]
//         }
//     });
// }

// async function fetchStatsAndUpdate() {
//     const countElement = document.getElementById("num");
//     const riskBox = document.getElementById("riskBox");
//     const alertBox = document.getElementById("alert");
//     const alarm = document.getElementById("alarmSound");

//     try {
//         const res = await fetch("/get_stats");
//         const data = await res.json();

//         const count = parseInt(data.count || 0);
//         countElement.innerText = count;

//         // Remove old classes
//         riskBox.classList.remove("safe", "intermediate", "high");

//         // SAFE
//         if (data.color === "green") {
//             riskBox.innerText = "SAFE";
//             riskBox.classList.add("safe");
//             alertBox.classList.add("hidden");

//             pieChart.data.datasets[0].data = [count, 0, 0];

//             // Stop alarm if running
//             alarm.pause();
//             alarm.currentTime = 0;
//             alarmPlayed = false;
//         }

//         // INTERMEDIATE
//         else if (data.color === "yellow") {
//             riskBox.innerText = "INTERMEDIATE";
//             riskBox.classList.add("intermediate");
//             alertBox.classList.add("hidden");

//             pieChart.data.datasets[0].data = [0, count, 0];

//             alarm.pause();
//             alarm.currentTime = 0;
//             alarmPlayed = false;
//         }

//         // HIGH RISK
//         else {
//             riskBox.innerText = "HIGH RISK";
//             riskBox.classList.add("high");
//             alertBox.classList.remove("hidden");

//             pieChart.data.datasets[0].data = [0, 0, count];

//             // Alarm Play
//             if (!alarmPlayed && alarmUnlocked) {
//                 alarm.play();
//                 alarmPlayed = true;
//             }
//         }

//         pieChart.update();

//         // Fake Male/Female Demo
//         let male = Math.floor(count * 0.6);
//         let female = count - male;

//         barChart.data.datasets[0].data = [male, female];
//         barChart.update();

//         // Area Chart Update
//         const timeLabel = new Date().toLocaleTimeString();
//         historyLabels.push(timeLabel);
//         historyData.push(count);

//         if (historyData.length > 10) {
//             historyData.shift();
//             historyLabels.shift();
//         }

//         areaChart.data.labels = historyLabels;
//         areaChart.data.datasets[0].data = historyData;
//         areaChart.update();

//     } catch (err) {
//         console.log("Error Fetching Stats:", err);
//     }
// }

// function startDashboardLoop() {
//     setInterval(fetchStatsAndUpdate, 1500);
// }

// function unlockAlarm() {
//     // Chrome autoplay restriction fix
//     const alarm = document.getElementById("alarmSound");

//     document.body.addEventListener("click", () => {
//         alarm.play().then(() => {
//             alarm.pause();
//             alarm.currentTime = 0;
//             alarmUnlocked = true;
//             console.log("Alarm unlocked!");
//         }).catch(() => {
//             console.log("Alarm still blocked by browser.");
//         });
//     }, { once: true });
// }

// window.onload = function () {
//     initCharts();
//     unlockAlarm();
//     startDashboardLoop();
// };









// let pieChart, barChart, areaChart;
// let historyData = [];
// let historyLabels = [];

// let alarmUnlocked = false;

// function initCharts() {
//     const pieCtx = document.getElementById("pieChart").getContext("2d");
//     const barCtx = document.getElementById("barChart").getContext("2d");
//     const areaCtx = document.getElementById("areaChart").getContext("2d");

//     pieChart = new Chart(pieCtx, {
//         type: "pie",
//         data: {
//             labels: ["Safe", "Intermediate", "High Risk"],
//             datasets: [{
//                 data: [0, 0, 0]
//             }]
//         }
//     });

//     barChart = new Chart(barCtx, {
//         type: "bar",
//         data: {
//             labels: ["Male", "Female"],
//             datasets: [{
//                 label: "Count",
//                 data: [0, 0]
//             }]
//         }
//     });

//     areaChart = new Chart(areaCtx, {
//         type: "line",
//         data: {
//             labels: [],
//             datasets: [{
//                 label: "Crowd Count",
//                 data: [],
//                 fill: true,
//                 tension: 0.3
//             }]
//         }
//     });
// }

// async function fetchStatsAndUpdate() {
//     const countElement = document.getElementById("num");
//     const riskBox = document.getElementById("riskBox");
//     const alertBox = document.getElementById("alert");
//     const alarm = document.getElementById("alarmSound");

//     try {
//         const res = await fetch("/get_stats");
//         const data = await res.json();

//         const count = parseInt(data.count || 0);
//         countElement.innerText = count;

//         // Remove old classes
//         riskBox.classList.remove("safe", "intermediate", "high");

//         // SAFE
//         if (data.color === "green") {
//             riskBox.innerText = "SAFE";
//             riskBox.classList.add("safe");
//             alertBox.classList.add("hidden");

//             pieChart.data.datasets[0].data = [count, 0, 0];

//             // Stop alarm
//             alarm.pause();
//             alarm.currentTime = 0;
//         }

//         // INTERMEDIATE
//         else if (data.color === "yellow") {
//             riskBox.innerText = "INTERMEDIATE";
//             riskBox.classList.add("intermediate");
//             alertBox.classList.add("hidden");

//             pieChart.data.datasets[0].data = [0, count, 0];

//             // Stop alarm
//             alarm.pause();
//             alarm.currentTime = 0;
//         }

//         // HIGH RISK
//         else {
//             riskBox.innerText = "HIGH RISK";
//             riskBox.classList.add("high");
//             alertBox.classList.remove("hidden");

//             pieChart.data.datasets[0].data = [0, 0, count];

//             // Continuous Alarm
//             if (alarmUnlocked) {
//                 alarm.loop = true;
//                 alarm.play().catch(() => {});
//             }
//         }

//         pieChart.update();

//         // Fake Male/Female Demo
//         let male = Math.floor(count * 0.6);
//         let female = count - male;

//         barChart.data.datasets[0].data = [male, female];
//         barChart.update();

//         // Area Chart Update
//         const timeLabel = new Date().toLocaleTimeString();
//         historyLabels.push(timeLabel);
//         historyData.push(count);

//         if (historyData.length > 10) {
//             historyData.shift();
//             historyLabels.shift();
//         }

//         areaChart.data.labels = historyLabels;
//         areaChart.data.datasets[0].data = historyData;
//         areaChart.update();

//     } catch (err) {
//         console.log("Error Fetching Stats:", err);
//     }
// }

// function startDashboardLoop() {
//     setInterval(fetchStatsAndUpdate, 1500);
// }

// function unlockAlarm() {
//     const alarm = document.getElementById("alarmSound");

//     // Chrome autoplay fix (User click required)
//     document.body.addEventListener("click", () => {
//         alarm.play().then(() => {
//             alarm.pause();
//             alarm.currentTime = 0;
//             alarmUnlocked = true;
//             console.log("Alarm unlocked successfully!");
//         }).catch(() => {
//             console.log("Alarm still blocked.");
//         });
//     }, { once: true });
// }

// window.onload = function () {
//     initCharts();
//     unlockAlarm();
//     startDashboardLoop();
// };









// let pieChart, barChart, areaChart;
// let historyData = [];
// let historyLabels = [];

// let alarmUnlocked = false;
// let manualMute = false;

// function initCharts() {
//     const pieCtx = document.getElementById("pieChart").getContext("2d");
//     const barCtx = document.getElementById("barChart").getContext("2d");
//     const areaCtx = document.getElementById("areaChart").getContext("2d");

//     pieChart = new Chart(pieCtx, {
//         type: "pie",
//         data: {
//             labels: ["Safe", "Intermediate", "High Risk"],
//             datasets: [{
//                 data: [0, 0, 0]
//             }]
//         }
//     });

//     barChart = new Chart(barCtx, {
//         type: "bar",
//         data: {
//             labels: ["Male", "Female"],
//             datasets: [{
//                 label: "Count",
//                 data: [0, 0]
//             }]
//         }
//     });

//     areaChart = new Chart(areaCtx, {
//         type: "line",
//         data: {
//             labels: [],
//             datasets: [{
//                 label: "Crowd Count",
//                 data: [],
//                 fill: true,
//                 tension: 0.3
//             }]
//         }
//     });
// }

// async function updateDashboard() {
//     const countElement = document.getElementById("num");
//     const riskBox = document.getElementById("riskBox");
//     const alertBox = document.getElementById("alert");
//     const stopBtn = document.getElementById("stopAlarmBtn");
//     const alarm = document.getElementById("alarmSound");

//     try {
//         const res = await fetch("/get_stats");
//         const data = await res.json();

//         const count = parseInt(data.count || 0);
//         countElement.innerText = count;

//         // Reset Risk classes
//         riskBox.classList.remove("safe", "intermediate", "high");

//         // SAFE
//         if (data.color === "green") {
//             riskBox.innerText = "SAFE";
//             riskBox.classList.add("safe");

//             alertBox.classList.add("hidden");
//             stopBtn.classList.add("hidden");

//             pieChart.data.datasets[0].data = [count, 0, 0];

//             alarm.pause();
//             alarm.currentTime = 0;
//             manualMute = false;
//         }

//         // INTERMEDIATE
//         else if (data.color === "yellow") {
//             riskBox.innerText = "INTERMEDIATE";
//             riskBox.classList.add("intermediate");

//             alertBox.classList.add("hidden");
//             stopBtn.classList.add("hidden");

//             pieChart.data.datasets[0].data = [0, count, 0];

//             alarm.pause();
//             alarm.currentTime = 0;
//             manualMute = false;
//         }

//         // HIGH RISK
//         else {
//             riskBox.innerText = "HIGH RISK";
//             riskBox.classList.add("high");

//             alertBox.classList.remove("hidden");
//             stopBtn.classList.remove("hidden");

//             pieChart.data.datasets[0].data = [0, 0, count];

//             if (alarmUnlocked && !manualMute) {
//                 alarm.loop = true;
//                 alarm.play().catch(() => {});
//             }
//         }

//         pieChart.update();

//         // Fake Male/Female Demo
//         let male = Math.floor(count * 0.6);
//         let female = count - male;

//         barChart.data.datasets[0].data = [male, female];
//         barChart.update();

//         // Area chart history
//         const timeLabel = new Date().toLocaleTimeString();
//         historyLabels.push(timeLabel);
//         historyData.push(count);

//         if (historyData.length > 10) {
//             historyLabels.shift();
//             historyData.shift();
//         }

//         areaChart.data.labels = historyLabels;
//         areaChart.data.datasets[0].data = historyData;
//         areaChart.update();

//     } catch (err) {
//         console.log("Error Fetching Stats:", err);
//     }
// }

// function unlockAlarmSystem() {
//     const alarm = document.getElementById("alarmSound");

//     document.addEventListener("click", () => {
//         alarm.play().then(() => {
//             alarm.pause();
//             alarm.currentTime = 0;
//             alarmUnlocked = true;
//             console.log("Alarm unlocked successfully!");
//         }).catch(() => {
//             console.log("Autoplay blocked by browser.");
//         });
//     }, { once: true });
// }

// function setupStopButton() {
//     document.getElementById("stopAlarmBtn").addEventListener("click", () => {
//         const alarm = document.getElementById("alarmSound");
//         alarm.pause();
//         alarm.currentTime = 0;
//         manualMute = true;
//     });
// }

// window.onload = function () {
//     initCharts();
//     unlockAlarmSystem();
//     setupStopButton();

//     setInterval(updateDashboard, 1500);
// };











let pieChart, barChart, areaChart;
let historyData = [];
let historyLabels = [];

let manualMute = false;

function initCharts() {
    const pieCtx = document.getElementById("pieChart").getContext("2d");
    const barCtx = document.getElementById("barChart").getContext("2d");
    const areaCtx = document.getElementById("areaChart").getContext("2d");

    pieChart = new Chart(pieCtx, {
        type: "pie",
        data: {
            labels: ["Safe", "Intermediate", "High Risk"],
            datasets: [{
                data: [0, 0, 0]
            }]
        }
    });

    barChart = new Chart(barCtx, {
        type: "bar",
        data: {
            labels: ["Male", "Female"],
            datasets: [{
                label: "Count",
                data: [0, 0]
            }]
        }
    });

    areaChart = new Chart(areaCtx, {
        type: "line",
        data: {
            labels: [],
            datasets: [{
                label: "Crowd Count",
                data: [],
                fill: true,
                tension: 0.3
            }]
        }
    });
}

async function updateDashboard() {
    const countElement = document.getElementById("num");
    const riskBox = document.getElementById("riskBox");
    const alertBox = document.getElementById("alert");
    const stopBtn = document.getElementById("stopAlarmBtn");

    try {
        const res = await fetch("/get_stats");
        const data = await res.json();

        const count = parseInt(data.count || 0);
        countElement.innerText = count;

        riskBox.classList.remove("safe", "intermediate", "high");

        if (data.color === "green") {
            riskBox.innerText = "SAFE";
            riskBox.classList.add("safe");
            alertBox.classList.add("hidden");
            stopBtn.classList.add("hidden");

            pieChart.data.datasets[0].data = [count, 0, 0];
            manualMute = false;
        }
        else if (data.color === "yellow") {
            riskBox.innerText = "INTERMEDIATE";
            riskBox.classList.add("intermediate");
            alertBox.classList.add("hidden");
            stopBtn.classList.add("hidden");

            pieChart.data.datasets[0].data = [0, count, 0];
            manualMute = false;
        }
        else {
            riskBox.innerText = "HIGH RISK";
            riskBox.classList.add("high");
            alertBox.classList.remove("hidden");
            stopBtn.classList.remove("hidden");

            pieChart.data.datasets[0].data = [0, 0, count];
        }

        pieChart.update();

        // Fake Male/Female
        let male = Math.floor(count * 0.6);
        let female = count - male;

        barChart.data.datasets[0].data = [male, female];
        barChart.update();

        // Area chart history
        const timeLabel = new Date().toLocaleTimeString();
        historyLabels.push(timeLabel);
        historyData.push(count);

        if (historyData.length > 10) {
            historyLabels.shift();
            historyData.shift();
        }

        areaChart.data.labels = historyLabels;
        areaChart.data.datasets[0].data = historyData;
        areaChart.update();

    } catch (err) {
        console.log("Error Fetching Stats:", err);
    }
}

function setupStopButton() {
    document.getElementById("stopAlarmBtn").addEventListener("click", async () => {
        await fetch("/stop_alarm", { method: "POST" });
        manualMute = true;
        alert("Alarm Stopped Successfully!");
    });
}

window.onload = function () {
    initCharts();
    setupStopButton();
    setInterval(updateDashboard, 1500);
};

