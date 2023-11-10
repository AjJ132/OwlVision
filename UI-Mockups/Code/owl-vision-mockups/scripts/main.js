window.onload = function () {
  // Check if the 'visited' token is in localStorage
  if (!localStorage.getItem("visited")) {
    // It's the user's first visit, display the popup and overlay
    document.getElementById("overlay").classList.add("fade-in");
    document.getElementById("popupCard").classList.add("fade-in");

    document.getElementById("overlay").style.display = "block";
    document.getElementById("popupCard").style.display = "block";

    // Set the 'visited' token in localStorage
    localStorage.setItem("visited", "true");
  }

  // Dismiss button functionality
  document.getElementById("dismissButton").onclick = function () {
    var overlay = document.getElementById("overlay");
    var popupCard = document.getElementById("popupCard");

    overlay.classList.replace("fade-in", "fade-out");
    popupCard.classList.replace("fade-in", "fade-out");

    setTimeout(function () {
      overlay.style.display = "none";
      popupCard.style.display = "none";
    }, 500); // Match this timeout with the animation-duration
  };
};

document.addEventListener("DOMContentLoaded", (event) => {
  const gameDropdown = document.querySelector("#gameDropdown");
  const gameOptions = [
    "All",
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
          data: [127, 393, 645, 495, 248], // Replace these numbers with your actual data
          backgroundColor: [
            "rgba(255, 198, 41, 1)",
            "rgba(176, 179, 178, 1)",
            "rgba(255, 198, 41, 1)",
            "rgba(176, 179, 178, 1)",
            "rgba(255, 198, 41, 1)",
          ],
          borderColor: [
            "rgba(255, 198, 41, 1)",
            "rgba(176, 179, 178, 1)",
            "rgba(255, 198, 41, 1)",
            "rgba(176, 179, 178, 1)",
            "rgba(255, 198, 41, 1)",
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
          borderColor: "rgba(255, 198, 41, 1)",
          tension: 0.2,
        },
        {
          label: "Attended",
          data: [9000, 9200, 9100],
          fill: true,
          borderColor: "rgba(176, 179, 178, 1)",
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
