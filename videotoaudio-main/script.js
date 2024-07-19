// console.log(``);

let videoInput = document.getElementById("video");
let convertBtn = document.querySelector(".convert");
let videoName = document.querySelector(".videoName");
let play_download = document.querySelector(".play_download");
let playBtn = document.querySelector(".play");
let audio = new Audio();
let played = false;
videoInput.addEventListener("change", (e) => {
  let videoFile = e.target.files[0];
  let videoOriginalName = videoFile.name;
  let realVideoName = videoOriginalName.split(".mp4").join("");
  if (!videoFile) {
    alert(`Please Choose Video File`);
  } else {
    convertBtn.style.display = "block";
    videoName.style.display = `block`;
    videoName.innerHTML = `Video Name - ${realVideoName}`;

    convertBtn.addEventListener("click", () => {
      let url = URL.createObjectURL(videoFile);
      if (!url) {
        alert(`Please Choose Video File`);
        play_download.style.display = "none";
      } else {
        play_download.style.display = "block";

        audio.src = url;

        playBtn.addEventListener("click", () => {
          if (!played) {
            audio.play();
            playBtn.innerHTML = `Pause`;
            played = true;
          } else {
            audio.pause();
            playBtn.innerHTML = `Play`;
            played = false;
          }
        });

        audio.addEventListener('ended', () => {
            audio.pause();
            playBtn.innerHTML = `Play`;
            played = false;
        })
      }
    });
  }
});