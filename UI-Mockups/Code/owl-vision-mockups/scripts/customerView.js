document.addEventListener("DOMContentLoaded", (event) => {
  //line chart to show purchased tickets vs people who did not show
  const actualAttendanceComparisonChart = document
    .getElementById("customer-attendence-line-chart")
    .getContext("2d");
  const aacLineChart = new Chart(actualAttendanceComparisonChart, {
    type: "line",
    data: {
      labels: ["2020", "2021", "2022", "2023"],
      datasets: [
        {
          label: "Purchased",
          data: [2, 4, 4, 5],
          fill: true,
          borderColor: "rgba(255, 198, 41, 1)",
          tension: 0.2,
        },
        {
          label: "Attended",
          data: [2, 3, 4, 4],
          fill: true,
          borderColor:"rgba(176, 179, 178, 1)",
          tension: 0.2,
        },
      ],
    },
    options: {
      animation: {
        duration: 2000
      },
      scales: {
        y: {
          beginAtZero: true,
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

  //doughnut chart to show percentile for ST rating
  const percentileSTRatingEle = document
    .getElementById("percentileSTRating")
    .getContext("2d");
  const percentileSTRatingPieChart = new Chart(percentileSTRatingEle, {
    type: "doughnut",
    data: {
      // labels: ["Customer Percentile"],
      datasets: [
        {
          label: "Attendance Percentile",
          data: [95, 5], // Replace these numbers with your actual data
          backgroundColor: [
            "rgba(255, 198, 41, 1)",
            "rgba(176, 179, 178, 1)",
            
          ],
          borderColor: [
            "rgba(255, 198, 41, 1)",
            "rgba(176, 179, 178, 1)",
            
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      // showlabels: false,
      animation: {
        duration: 2000
      },
      responsive: false,
          maintainAspectRatio: true,
      // scales: {
      //   y: {
      //     beginAtZero: true,
          
      //     ticks: {
      //       // Include a dollar sign in the ticks and ensure whole numbers only
      //       callback: function (value) {
      //         if (value % 1 === 0) {
      //           return value;
      //         }
      //       },
      //     },
      //   },
      // },
    },
  });

  //doughnut chart to show percentile for ST rating
  const percentileAttendenceEle = document
    .getElementById("percentileAttendence")
    .getContext("2d");
  const percentileAttendencePieChart = new Chart(percentileAttendenceEle, {
    type: "doughnut",
    data: {
      // labels: ["Customer Percentile"],
      datasets: [
        {
          label: "ST Percentile Rating",
          data: [83, 17], // Replace these numbers with your actual data
          backgroundColor: [
            "rgba(255, 198, 41, 1)",
            "rgba(176, 179, 178, 1)",
            
          ],
          borderColor: [
            "rgba(255, 198, 41, 1)",
            "rgba(176, 179, 178, 1)",
            
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      // showlabels: false,
      animation: {
        duration: 2000
      },
      responsive: false,
          maintainAspectRatio: true,
      // scales: {
      //   y: {
      //     beginAtZero: true,
          
      //     ticks: {
      //       // Include a dollar sign in the ticks and ensure whole numbers only
      //       callback: function (value) {
      //         if (value % 1 === 0) {
      //           return value;
      //         }
      //       },
      //     },
      //   },
      // },
    },
  });

  //doughnut chart to show percentile for ST rating
  const percentileSocialInteractionsEle = document
    .getElementById("percentileSocialInteractions")
    .getContext("2d");
  const percentileSocialInteractionPieChart = new Chart(percentileSocialInteractionsEle, {
    type: "doughnut",
    data: {
      // labels: ["Customer Percentile"],
      datasets: [
        {
          label: "ST Percentile Rating",
          data: [45, 55], // Replace these numbers with your actual data
          backgroundColor: [
            "rgba(255, 198, 41, 1)",
            "rgba(176, 179, 178, 1)",
            
          ],
          borderColor: [
            "rgba(255, 198, 41, 1)",
            "rgba(176, 179, 178, 1)",
            
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      // showlabels: false,
      animation: {
        duration: 2000
      },
      responsive: false,
          maintainAspectRatio: true,
      // scales: {
      //   y: {
      //     beginAtZero: true,
          
      //     ticks: {
      //       // Include a dollar sign in the ticks and ensure whole numbers only
      //       callback: function (value) {
      //         if (value % 1 === 0) {
      //           return value;
      //         }
      //       },
      //     },
      //   },
      // },
    },
  });

  
});
