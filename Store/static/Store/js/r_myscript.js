// var nav = document.querySelector('nav')
// window.addEventListener('scroll', function(){
//     if(window.pageYOffset > 100){
//         nav.classList.add('bg-dark', 'shadow')
//     }else{
//         nav.classList.remove('bg-dark', 'shadow')
//     }
// })
let index_new = document.querySelector("#index_new")
let index_trend = document.querySelector("#index_trend")
let index_favorite = document.querySelector("#index_favorite")
let section_index_new = document.querySelector("#section_index_new")
let section_index_trend = document.querySelector("#section_index_trend")
let section_index_favorite = document.querySelector("#section_index_favorite")
index_new.addEventListener('click',function () {
    section_index_trend.classList.add("d-none")
    section_index_favorite.classList.add("d-none")
    section_index_new.classList.remove("d-none")
})
index_trend.addEventListener("click", function(e){
    section_index_trend.classList.remove("d-none")
    section_index_favorite.classList.add("d-none")
    section_index_new.classList.add("d-none")
})
index_favorite.addEventListener("click", function(e){
    section_index_favorite.classList.remove("d-none")
    section_index_trend.classList.add("d-none")
    section_index_new.classList.add("d-none")
})

// let .r-play-link
let r_play_links = document.querySelectorAll(".r-play-link")
// let .played-badge-circle
let  r_disk_played_circle_demos = document.querySelectorAll(".r-disk-played-circle-demo")
let  r_disk_played_icon = document.querySelectorAll(".r-disk-played-icon")
for (let index = 0; index < r_play_links.length; index++) {
    r_play_links[index].addEventListener("click", function () {
        for (let i = 0; i < r_disk_played_circle_demos.length; i++) {
            r_disk_played_circle_demos[i].classList.add("d-none")
            r_disk_played_icon[i].classList.add("d-none")
        }
    r_disk_played_circle_demos[index].classList.remove("d-none")
    r_disk_played_icon[index].classList.remove("d-none")
    })
}
// #joinus .container .w-100 form .r-before-email-form
let r_before_email_form = document.querySelector("#joinus .container .w-100 form .r-before-email-form")
let r_form_div = document.querySelector("#joinus .container .w-100 form .r-form-div")
// let #joinus .container .w-100 form .r-form-div
r_before_email_form.addEventListener("click",function () {
    r_before_email_form.classList.add("d-none")
    r_form_div.classList.remove("d-none")
})
