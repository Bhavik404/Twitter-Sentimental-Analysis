// var months = ["January","February","March","April","May","June","July","August","September","October"]
var options = {
  series: [{
  name: 'Positive',
  data: positive_barchart
}, {
  name: 'Neutral',
  data: neutral_barchart
}, {
  name: 'Negative',
  data: negative_barchart
}],
  chart: {
  type: 'bar',
  height: 350
},
colors: ['#2abb2a', '#eeae00', "#e60023"],
plotOptions: {
  bar: {
    horizontal: false,
    columnWidth: '50%',
    borderRadius: 5,
    endingShape: 'rounded'
  },
},
dataLabels: {
  enabled: false
},
stroke: {
  show: true,
  width: 2,
  colors: ['transparent']
},
xaxis: {
  categories: ["Week 1","Week 2","Week 3","Week 4"],
},
yaxis: {
  title: {
    text: 'Sentiments'
  }
},
fill: {
  opacity: 1,
  colors: ['#00E396', '#FEB019', '#FA4443']
},
// tooltip: {
//   y: {
//     formatter: function (val) {
//       return "$ " + val + " thousands"
//     }
//   }
// }
};

var chart = new ApexCharts(document.querySelector("#apex_bar_chart"), options);
chart.render();

// pie chart

var options2 = {
  series: pie_data,
  chart: {
    width: 380,
    type: 'pie',
  },
  colors: ['#00E396', '#FEB019', '#FA4443'],
  labels: ['Positive', 'Neutral', 'Negative'],
  responsive: [
    {
      breakpoint: 480,
      options: {
        chart: {
          width: 200,
        },
        legend: {
          position: 'bottom',
        },
      },
    },
  ],
};

var chart2 = new ApexCharts(document.querySelector('#apex_pie_chart'), options2);
chart2.render();

// doughnut chart
var options3 = {
  series: pie_data,
  chart: {
    type: 'donut',
    width: 380,
  },
  colors: ['#00E396', '#FEB019', '#FA4443'],
  labels: ['Positive', 'Neutral', 'Negative'],
  responsive: [
    {
      breakpoint: 480,
      options: {
        chart: {
          width: 200,
        },
        legend: {
          position: 'bottom',
        },
      },
    },
  ],
};

var chart3 = new ApexCharts(document.querySelector('#apex_doughnut_chart'), options3);
chart3.render();

// line chart

var options4 = {
  series: [
  {
    name: "Positive",
    data: Positive_linechart
  },
  {
    name: "Neutral",
    data: Neutral_linechart
  },
  {
    name: "Negative",
    data: Negative_linechart
  }
],
  chart: {
  height: 350,
  type: 'line',
  dropShadow: {
    enabled: true,
    color: '#000',
    top: 18,
    left: 7,
    blur: 10,
    opacity: 0.2
  },
  toolbar: {
    show: true
  }
},
colors: ['#2abb2a', '#eeae00', "#e60023"],
dataLabels: {
  enabled: true,
},
stroke: {
  curve: 'smooth'
},
title: {
  text: 'Line graph showing sentiments of months',
  align: 'left'
},
grid: {
  borderColor: '#e7e7e7',
  row: {
    colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
    opacity: 0.5
  },
},
markers: {
  size: 1
},
xaxis: {
  categories: months,
  title: {
    text: 'Month'
  }
},
yaxis: {
  title: {
    text: 'Sentiments'
  },
  min: 0,
  function(max) { return max }
},
legend: {
  position: 'top',
  horizontalAlign: 'right',
  floating: true,
  offsetY: -25,
  offsetX: -5
}
};

var chart4 = new ApexCharts(document.querySelector("#apex_line_chart"), options4);
chart4.render();

// WORD CLOUD
anychart.onDocumentReady(function () {
  var data = cloud;
          	// create tag cloud
  var chart = anychart.tagCloud();

            // set data with settings
  chart.data(data,{
    mode: "byWord",
    maxItems: 70,
    ignoreItems: [
                  "the",
                  "and",
                  "he",
                  "or",
                  "of",
                  "in",
                  "thy"
                 ]
});

            // set array of angles, by which words will be placed
  chart.angles([0]);
            // additional empty space in all directions from the text, only in pixels
  chart.textSpacing(1);

            // set container id for the chart
  chart.container('tagcloud');
            // initiate chart drawing
  chart.draw();
});

// TOP 10 WORDS CHART
var options = {
  series: [{
  data: top10words_count
}],
  chart: {
  type: 'bar',
  height: 350
},
plotOptions: {
  bar: {
    borderRadius: 4,
    horizontal: true,
  }
},
colors: ['#90ee7e'],
dataLabels: {
  enabled: false
},
xaxis: {
  categories: top10words,
}
};

var chart = new ApexCharts(document.querySelector("#top10"), options);
chart.render();

// TOP ORGANIZATIONS MENTIONED
var options = {
  series: [{
  data: orgs_count
}],
  chart: {
  type: 'bar',
  height: 350
},
plotOptions: {
  bar: {
    borderRadius: 4,
    horizontal: true,
  }
},
colors: ['#13d8aa'],
dataLabels: {
  enabled: false
},
xaxis: {
  categories: orgs,
}
};

var chart = new ApexCharts(document.querySelector("#toporg"), options);
chart.render();

// var options = {
//   series: [{
//   data: orgs_count
// }],
//   chart: {
//   type: 'bar',
//   height: 380
// },
// plotOptions: {
//   bar: {
//     barHeight: '100%',
//     borderRadius: 4,
//     distributed: true,
//     horizontal: true,
//     dataLabels: {
//       position: 'bottom'
//     },
//   }
// },
// colors: ['#33b2df', '#546E7A', '#d4526e', '#13d8aa', '#A5978B', '#2b908f', '#f9a3a4', '#90ee7e',
//   '#f48024', '#69d2e7'],
// dataLabels: {
//   enabled: true,
//   textAnchor: 'start',
//   style: {
//     colors: ['#fff']
//   },
//   formatter: function (val, opt) {
//     return opt.w.globals.labels[opt.dataPointIndex] + ":  " + val
//   },
//   offsetX: 0,
//   dropShadow: {
//     enabled: true
//   }
// },
// stroke: {
//   width: 1,
//   colors: ['#fff']
// },
// xaxis: {
//   categories: orgs,
// },
// yaxis: {
//   labels: {
//     show: false
//   }
// },
// title: {
//     text: 'Custom DataLabels',
//     align: 'center',
//     floating: true
// },
// subtitle: {
//     text: 'Category Names as DataLabels inside bars',
//     align: 'center',
// },
// tooltip: {
//   theme: 'dark',
//   x: {
//     show: false
//   },
//   y: {
//     title: {
//       formatter: function () {
//         return ''
//       }
//     }
//   }
// }
// };

// var chart = new ApexCharts(document.querySelector("#toporg"), options);
// chart.render();

