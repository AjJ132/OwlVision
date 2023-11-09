document.addEventListener("DOMContentLoaded", (event) => {
  const gameDropdown = document.querySelector("#gameDropdown");
  const gameOptions = [
    "Lincoln | 10/28",
    "Tennessee State | 10/07",
    "Furman | 08/16",
  ]; // Sample options

  gameOptions.forEach((option) => {
    const optElement = document.createElement("option");
    optElement.value = option;
    optElement.textContent = option;
    gameDropdown.appendChild(optElement);
  });

  const aacDropdown = document.querySelector("#aacOptionsDropdown");
  const aacOptions = ["All", "Students", "Season Ticket Holders"]; // Sample options

  aacOptions.forEach((option) => {
    const optElement = document.createElement("option");
    optElement.value = option;
    optElement.textContent = option;
    aacDropdown.appendChild(optElement);
  });

  //Bar Chart for ST Ratings

  const ctx = document.getElementById("scoreChart").getContext("2d");
  const scoreChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["0-1", "1-2", "2-3", "3-4", "4-5"],
      datasets: [
        {
          label: "ST Ratings",
          data: [5, 10, 15, 20, 25], // Replace these numbers with your actual data
          backgroundColor: [
            "rgba(255, 99, 132, 0.65)",
            "rgba(54, 162, 235, 0.65)",
            "rgba(255, 206, 86, 0.65)",
            "rgba(75, 192, 192, 0.65)",
            "rgba(153, 102, 255, 0.65)",
          ],
          borderColor: [
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
            "rgba(153, 102, 255, 1)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
          ticks: {
            // Include a dollar sign in the ticks and ensure whole numbers only
            callback: function (value) {
              if (value % 1 === 0) {
                return value;
              }
            },
          },
        },
      },
    },
  });

  //line chart to show purchased tickets vs people who did not show
  const actualAttendanceComparisonChart = document
    .getElementById("aacLineChart")
    .getContext("2d");
  const aacLineChart = new Chart(actualAttendanceComparisonChart, {
    type: "line",
    data: {
      labels: ["Lincoln | 10/28", "Tennessee State | 10/07", "Furman | 08/16"],
      datasets: [
        {
          label: "Purchased",
          data: [9500, 9700, 9400],
          fill: true,
          borderColor: "rgb(75, 192, 192)",
          tension: 0.2,
        },
        {
          label: "Attended",
          data: [9000, 9200, 9100],
          fill: true,
          borderColor: "rgb(255, 99, 132)",
          tension: 0.2,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: false,
          gridLines: {
            display: true,
          },
          scaleLabel: {
            display: true,
            labelString: "Number of Attendees",
          },
        },
        x: {
          gridLines: {
            display: false,
          },
        },
      },
      tooltips: {
        mode: "index",
        intersect: false,
      },
      hover: {
        mode: "nearest",
        intersect: true,
      },
      legend: {
        position: "top",
      },
      title: {
        display: true,
        text: "Attendance Comparison",
      },
    },
  });
});
