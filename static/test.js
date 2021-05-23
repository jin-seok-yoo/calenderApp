var container = document.getElementById('lottie');
const intro = document.querySelector(".wrapper");

// animData = lottie.loadAnimation({
//     container: container,
//     renderer: 'svg',
//     autoplay: false,
//     loop: false,
//     rendererSettings: {
//         progressiveLoad:false,
//         preserveAspectRatio: 'xMidYMid slice'
//     },
//     path : jsonPath
// });

//SCROLLMAGIC
const controller = new ScrollMagic.Controller();

//Scenes
let scene = new ScrollMagic.Scene({
duration: 5000,
triggerElement: intro,
triggerHook: 0
})
    .addIndicators()
    .setPin(intro)
    .addTo(controller);

const scrollbar = Scrollbar.init(intro, {
    renderByPixels: false
});

let lottieProgress = lottie.loadAnimation({
    container: container,
    renderer: "svg",
    loop: false,
    autoplay: false,
    path: jsonPath
});

scrollbar.addListener(() => {
    let totalHeight = scrollbar.limit.y;
    let scrollFromTop = scrollbar.scrollTop;
    let scrollPercentage = (scrollFromTop * 100) / totalHeight;
    let scrollPercentRounded = Math.round(scrollPercentage); // Just in case
    lottieProgress.goToAndStop(
        (scrollPercentage * lottieProgress.totalFrames) / 100,
        true
    );
});

scrollbar.scrollTo(0, 700, 2000);


// //Video Animation
// let accelamount = 0.1;
// let scrollpos = 0;
// let delay = 0;

// scene.on("update", e => {
//     scrollpos = e.scrollPos / 1000;
// });

// setInterval(() => {
//     delay += (scrollpos - delay) * accelamount;
//     console.log(scrollpos, delay);
//     // video.currentTime = delay;
//     animData.playSegments([animationStart,animationStart+1], true);
//     animationStart++;
// }, 33.3);



// var animationStart = 0;
// window.__scrollPosition = document.documentElement.scrollTop || 0;
// $(window).scroll(function(){

//     let _documentY = document.documentElement.scrollTop;
//     let _direction = _documentY - window.__scrollPosition >= 0 ? 1 : -1;
//     console.log(_direction); // 콘솔창에 스크롤 방향을 출력
//     window.__scrollPosition = _documentY; // Update scrollY

//     animData.playSegments([animationStart,animationStart+1], true);
//     animationStart++;

// });