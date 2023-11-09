document.addEventListener("DOMContentLoaded", (event) => {
  const pieChart1 = document
    .getElementById("stAttendenceVsRegularFans")
    .getContext("2d");
  const stAttendenceVsRegularFans = new Chart(pieChart1, {
    type: "pie", // Define the chart type
    data: {
      labels: ["Regular Fans", "Season Ticket Holders", "Students"],
      datasets: [
        {
          label: "ST Attendance vs Other Fans",
          data: [60, 20, 20], // Data for the pie chart
          backgroundColor: [
            "rgba(54, 162, 235, 0.65)", // Color for regular fans
            "rgba(255, 159, 64, 0.65)", // Color for season ticket holders
            "rgba(255, 99, 132, 0.65)", // Color for students
          ],
          borderColor: ["rgba(54, 162, 235, 1)", "rgba(255, 159, 64, 1)"],
          borderWidth: 1,
        },
      ],
    },
    options: {
      plugins: {
        datalabels: {
          color: "#fff",
          textAlign: "center",
          font: {
            weight: "bold",
          },
          formatter: (value, ctx) => {
            return `${value}%`;
          },
        },
      },
      responsive: false,
      maintainAspectRatio: true,
      title: {
        display: true,
        text: "ST Attendance vs Other Fans",
        fontSize: 18,
        fontStyle: "bold",
      },
    },
  });

  const studentsPieChartElement = document
    .getElementById("studentsPieChart")
    .getContext("2d");
  const studentsPieChart = new Chart(studentsPieChartElement, {
    type: "pie", // Define the chart type
    data: {
      labels: ["Other Fans", "Students"],
      datasets: [
        {
          label: "Students vs Regular Fans",
          data: [80, 20], // Data for the pie chart
          backgroundColor: [
            "rgba(54, 162, 235, 0.65)", // Color for regular fans
            "rgba(255, 159, 64, 0.65)", // Color for season ticket holders
          ],
          borderColor: ["rgba(54, 162, 235, 1)", "rgba(255, 159, 64, 1)"],
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: false,
      maintainAspectRatio: true,
      title: {
        display: true,
        text: "ST Attendance vs Regular Fans",
      },
    },
  });
});
