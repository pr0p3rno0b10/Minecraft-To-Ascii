// so far not working

const imageToAscii = require("image-to-ascii");
const fs = require('fs')

var filepathArray;



var filepath = "textures/blocks/grass_side.png";
ascifiedImage = imageToAscii(filepath, (err, converted) => {
    console.log(err || converted);
});


const content = ascifiedImage;

fs.writeFile('/Users/joe/test.txt', content, err => {
  if (err) {
    console.error(err)
    return
  }
})