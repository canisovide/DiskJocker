let r_listing_typing_text = document.querySelector("#listing_typing_text")
let i= 0
let speed = 100
let text = "Découvrez nos divers disques et écoutez de la bonne musique chez vous tout en réservant vos disques chez nous."
function typing() {

    r_listing_typing_text.innerHTML+=text.charAt(i);
    i++;
    setTimeout(typing, speed);
    // setInterval(typing, speed)
    console.log("called")
}
typing();