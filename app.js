/*const images = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsEFTJyiprf8CPYc_WaV6T97zrPVleDAMtnbkdb9kEA&s=Image+1",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsEFTJyiprf8CPYc_WaV6T97zrPVleDAMtnbkdb9kEA&s=Image+2",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsEFTJyiprf8CPYc_WaV6T97zrPVleDAMtnbkdb9kEA&s=Image+3",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsEFTJyiprf8CPYc_WaV6T97zrPVleDAMtnbkdb9kEA&s=Image+4",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsEFTJyiprf8CPYc_WaV6T97zrPVleDAMtnbkdb9kEA&s=Image+5",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsEFTJyiprf8CPYc_WaV6T97zrPVleDAMtnbkdb9kEA&s=Image+6",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsEFTJyiprf8CPYc_WaV6T97zrPVleDAMtnbkdb9kEA&s=Image+7",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsEFTJyiprf8CPYc_WaV6T97zrPVleDAMtnbkdb9kEA&s=Image+8",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsEFTJyiprf8CPYc_WaV6T97zrPVleDAMtnbkdb9kEA&s=Image+8",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsEFTJyiprf8CPYc_WaV6T97zrPVleDAMtnbkdb9kEA&s=Image+8",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsEFTJyiprf8CPYc_WaV6T97zrPVleDAMtnbkdb9kEA&s=Image+8",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsEFTJyiprf8CPYc_WaV6T97zrPVleDAMtnbkdb9kEA&s=Image+8",
   
];

let visibleItems = 4;

document.addEventListener("DOMContentLoaded", () => {
    loadInitialItems();
});

function loadInitialItems() {
    const content = document.getElementById("content");
    for (let i = 0; i < visibleItems; i++) {
        const itemDiv = document.createElement("div");
        itemDiv.classList.add("item");
        const img = document.createElement("img");
        img.src = images[i];
        itemDiv.appendChild(img);
        content.appendChild(itemDiv);
    }
}

function loadMore() {
    const content = document.getElementById("content");
    const currentItems = content.children.length;
    for (let i = currentItems; i < currentItems + visibleItems && i < images.length; i++) {
        const itemDiv = document.createElement("div");
        itemDiv.classList.add("item");
        const img = document.createElement("img");
        img.src = images[i];
        itemDiv.appendChild(img);
        content.appendChild(itemDiv);
    }

    if (content.children.length >= images.length) {
        document.getElementById("loadMore").style.display = "none";
    }
}
*/

/*const counters = document.querySelectorAll('.counter');
const speed = 200; // The lower the slower

counters.forEach(counter => {
  const updateCount = () => {
    const target = +counter.getAttribute('data-target');
    const count = +counter.innerText;

    // Lower inc to slow and higher to slow
    const inc = target / speed;

    // console.log(inc);
    // console.log(count);

    // Check if target is reached
    if (count < target) {
      // Add inc to count and output in counter
      counter.innerText = count + inc;
      // Call function every ms
      setTimeout(updateCount, 1);
    } else {
      counter.innerText = target;
    }
  };

  updateCount();
});
*/