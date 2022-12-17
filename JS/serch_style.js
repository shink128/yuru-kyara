console.log("三角形の面積は");
console.log(3*4/2);

$('button').click(function() {
    var A = $('input[name="radio_A"]:checked').val();
    var B = $('input[name="radio_B"]:checked').val();
    console.log(A+B);
    window.location.href = (A+B)+'.html';
})


$('input:radio[name="radio_A"]').change(function() {
    const str1 = $('input:radio[name="radio_A"]:checked').val();
    $('#span1').text(str1);
    // console.log(str1); 
    


console.log(`url(../img/`+str1+`.gif)`);

var div = document.getElementById('big_A');
div.style.backgroundImage = "url(../img/"+str1+".gif)";

});

$('input:radio[name="radio_B"]').change(function() {
    const str2 = $('input:radio[name="radio_B"]:checked').val();
    $('#span1').text(str2);
    // console.log(str1); 
    


console.log(`url(../img/`+str2+`.gif)`);

var div = document.getElementById('big_B');
div.style.backgroundImage = "url(../img/"+str2+".gif)";

});