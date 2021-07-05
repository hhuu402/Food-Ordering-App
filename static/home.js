function classAdd(element, name) {
  var arr;
  console.log(element.className);
  arr = element.className.split(" ");
  if (arr.indexOf(name) == -1) {
    element.className += " " + name;
  }
}

function classRemove(element, name) {
    console.log("Removing Class");
    console.log(element.className);
    element.className = element.className.replace(name, "");
}        
function displayGone() {
        this.style.display = "none";
        this.removeEventListener("transitionend", displayGone);
        this.removeEventListener("webkitTransitionEnd", displayGone);
}
var burger_elem = document.getElementById("burgers");
burger_elem.addEventListener("click", function(event){
    event.preventDefault();
    console.log("Button pressed");
    var elem = document.getElementsByClassName("img-2")[0];                 // image
    var elem1 = document.getElementsByClassName("flex-centering")[1];       // container holding text
    var elem2 = document.getElementsByClassName("aspect-ratio-inside")[1];  // container holding image
    var elem3 = document.getElementById("wraps");                           // container holding bg color
    console.log(elem3.style.display)
    if (elem3.style.display != "none") {                                    // Once animation complete, display = Non
        elem3.addEventListener("transitionend", displayGone);
        elem3.addEventListener("webkitTransitionEnd", displayGone);
        classAdd(elem, "vanish");
        classAdd(elem1, "vanish");
        classAdd(elem2, "transparent");
        classAdd(elem3, "vanish");
    }
    else {
        classRemove(elem, "vanish");
        classRemove(elem1, "vanish");
        classRemove(elem2, "transparent");
        classRemove(elem3, "vanish");
        elem3.style.display = "initial";
    }
});

var wrap_elem = document.getElementById("wraps");
wrap_elem.addEventListener("click", function(event){
    event.preventDefault();
    console.log("Button pressed");
    var elem = document.getElementsByClassName("img-1")[0];                 // image
    var elem1 = document.getElementsByClassName("flex-centering")[0];       // container holding text
    var elem2 = document.getElementsByClassName("aspect-ratio-inside")[0];  // container holding image
    var elem3 = document.getElementById("burgers");                         // container holding bg color
    console.log(elem3.style.display)
    if (elem3.style.display != "none") {                                    // Once animation complete, display = Non
        elem3.addEventListener("transitionend", displayGone);
        elem3.addEventListener("webkitTransitionEnd", displayGone);
        classAdd(elem, "vanish");
        classAdd(elem1, "vanish");
        classAdd(elem2, "transparent");
        classAdd(elem3, "vanish");
    }
    else {
        classRemove(elem, "vanish");
        classRemove(elem1, "vanish");
        classRemove(elem2, "transparent");
        classRemove(elem3, "vanish");
        elem3.style.display = "initial";
    }
});