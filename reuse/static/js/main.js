import { CountUp } from './countUp.min.js';

window.onload = function() {
  var count = parseFloat($('#target').text())
  console.log(count)
  const options = {
    decimalPlaces: 2,
    duration: 3
  };

  var countUp = new CountUp('target', count, options);
  countUp.start();
}
