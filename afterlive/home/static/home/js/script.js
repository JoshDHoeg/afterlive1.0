//we also want to create a variable that holds the current number of loaded items on the page.
var DisplayList = 0;
//create  avariable that stores the value of the scroll load loaction
var scroll_pos_test = 512;
//create a content list
var contentList = [];

//when the page loads start to load the first 12 elements
$( document ).ready(function() {
  createFunction(0);
  createFunction(3);
  createFunction(6);
  createFunction(9);
  console.log("AND RELIVE THE MUSIC");
});

/*---------------------------------------------------------------------------
Move Button Scripts
---------------------------------------------------------------------------*/
$("#right").click(function () {
  var leftPos = $('.tag-container').scrollLeft();
  $(".tag-container").animate({scrollLeft: leftPos + 400}, 300);
});

$("#left").click(function () {
  var leftPos2 = $('.tag-container').scrollLeft();
  $(".tag-container").animate({scrollLeft: leftPos2 - 400}, 250);
});

/*---------------------------------------------------------------------------
Visible and Hidden functions to easily hide and show content
----------------------------------------------------------------------------*/
//this function will make the element visible
var visible = function(id){
  var e = document.getElementById(id);
  //console.log(e.style.display);
  if( id === "selected-tags-container"){
    e.style.display = "block";
  }else{
  e.style.display = "inline";
}
  //console.log("toggled visibility on: " + e.style.diplay);
  //e.parentNode.className="col-sm-6 col-md-4 contentItem";
}
//this function will make the element disapear
var hidden = function(id){
  var e = document.getElementById(id);
  //console.log(e.style.display);
  e.style.display = "none";
  //console.log("toggled visibility off: " + e.style.diplay);
  //e.parentNode.className="hidden";
}

/*-----------------------------------------------------------------------------
Search for tags
-----------------------------------------------------------------------------*/
//whenever you type a letter into the input searchFunction
//this function will update the associated tags
$("#searchBar").keyup(function(event){
  //collect the form element
  var x = document.getElementById("searchBar").value.toLowerCase();
  //save the length of the input
  var l = x.length;
  //initialize the variable match, to tell if the input matches a tag
  var match = true;
  //keep the scrollbar to the left
  $("div.tag-container").scrollLeft(0);
  //for all the values in the tag_list
  for(var i = 0; i <tag_list.length; i ++){



    //compare the input to the substring of the tag with the same size as the input
    var t = tag_list[i].substring(0,l).toLowerCase();
    if(x === t){

        //if they are the same then set match to true and make the tag element visible
        match=true;
        visible(tag_list[i]);
        //console.log(document.getElementById("{{tag.title}}").style.display);

    }else if(selectedList.includes(tag_list[i])){
      console.log("tag is in the selectedList");
      visible(tag_list[i]);

    }else{
      //for(var k = 0; k < selectedList.length; k++){
        //if(tag_list[i].title === selectedList[k]){
          hidden(tag_list[i]);
        //}
      //}
        //else hide the tag item and set match to false
        match=false;
        //console.log(tag_list[i].title + " : is in the selectedList");
        //console.log(document.getElementById("{{tag.title}}").style.display);
    }
  }
});


/*------------------------------------------------------------------------------
create content
------------------------------------------------------------------------------*/
var createFunction = function(index){
  DisplayList = DisplayList + 3;
  if((contentList.length == 0)&&(selectedList.length == 0)){
    for(var i = index; i < index + 3; i++){
      //console.log("i: " + i + " DisplayList: " + DisplayList);
      if(i < contentListRoot.length){
        //console.log("There is another");
        //console.log("loop: " + i);
        //console.log(contentList[i].Catagory);
        var CC = document.createElement("div");
        var contentItem = document.createElement("iframe");
        if(contentListRoot[i].Catagory == "Youtube"){
          contentItem.src = contentListRoot[i].Content;
          //console.log(contentItem.src);
        }
        else{
          contentItem.src = contentListRoot[i].Content + "embed";
        }
        contentItem.width="auto";
        contentItem.height="auto";
        contentItem.setAttribute('allowFullScreen', 'true');
        contentItem.className="center-block";
        contentItem.scrolling="no";
        contentItem.allowtransparency="true";
        contentItem.id = contentListRoot[i].id;
        CC.appendChild(contentItem);
        CC.id = contentListRoot[i].id + "a";
        CC.className ="col-sm-6 col-md-4 contentItem";
        //console.log(CC.className);
        document.getElementById("content-container").appendChild(CC);
      }
      else{
        //console.log("No MORE");
      }
    }

  }
  else
  {
    for(var i = index; i < index + 3; i++){
      if(i < contentList.length){
        //console.log("loop: " + i);
        //console.log(contentList[i].Catagory);

        var CC = document.createElement("div");
        var contentItem = document.createElement("iframe");
        if(contentList[i].Catagory == "Youtube"){
          contentItem.src = contentList[i].Content;
          //console.log(contentItem.src);
        }
        else{
          contentItem.src = contentList[i].Content + "embed";
        }
        contentItem.width="auto";
        contentItem.height="auto";
        contentItem.setAttribute('allowFullScreen', 'true');
        contentItem.className="center-block";
        contentItem.scrolling="no";
        contentItem.allowtransparency="true";
        contentItem.id = contentList[i].id;
        CC.appendChild(contentItem);
        CC.id = contentList[i].id + "a";
        CC.className ="col-sm-6 col-md-4 contentItem";
        //console.log(CC.className);
        document.getElementById("content-container").appendChild(CC);
      }
      else{

        //console.log("No MORE");
      }
    }
  }
};


/*----------------------------------------------------------------------------
add checked content to list for display
-----------------------------------------------------------------------------*/
var doCheck = function(list){
  var parent = document.getElementById("content-container");
  //i need to clear the current set of Data on the webpage, this part removes all the cildren nodes of the
  //content container
  while (parent.hasChildNodes()) {
    parent.removeChild(parent.lastChild);
  }
  DisplayList = 0;
  scroll_pos_test = 512;
  //we then empty out the contelist and hope to fill it back up with appropriate content
  contentList = [];
  if(list.length == 0){
    createFunction(0);
    createFunction(3);
    createFunction(6);
    createFunction(9);
  }
  //we loop through all the content in the array contentlistroot
  for(var i = 0; i < contentListRoot.length; i++){
    //for each element in the root list we need look at all the elements in the search list
      /*if there is only one string in the search list then the function only has to check the content in the root list
      for a match to that one string
      */
      if(list.length == 1){
        if((contentListRoot[i].Artist == list[0])){
          //console.log("Artist: " + contentListRoot[i].Artist);
          //console.log("Venue: " + contentListRoot[i].Venue);
          //console.log("Festival: " + contentListRoot[i].Festival);
          addToList(contentListRoot[i]);
        }else{
          for(var k = 0; k < contentList.length; k++){
            if(contentList[k].id === contentListRoot[i]){
              contentList.pop(contentList[k]);
            }
          }
        }
      }
      else if(list.length == 2){
        if((contentListRoot[i].Artist == list[0])){
          if((contentListRoot[i].Artist == list[1])){
            addToList(contentListRoot[i]);
          }else{
            for(var k = 0; k < contentList.length; k++){
              if(contentList[k].id === contentListRoot[i]){
                contentList.pop(contentList[k]);
              }
            }
          }
        }
      }else if(list.length == 3){
        if((contentListRoot[i].Artist == list[0])){
          if((contentListRoot[i].Artist == list[1])){
            if((contentListRoot[i].Artist == list[2])){
              addToList(contentListRoot[i]);
            }else{
              for(var k = 0; k < contentList.length; k++){
                if(contentList[k].id === contentListRoot[i]){
                  contentList.pop(contentList[k]);
                }
              }
            }
          }
        }
      }else if(list.length > 3){
        return;
      }
  }
}


/*-----------------------------------------------------------------------------
add the content to the list
------------------------------------------------------------------------------*/
var addToList = function(object){
  var P = new Object();
  P.Catagory = object.Catagory;
  P.Content = object.Content;
  P.Artist = object.Artist;
  P.Venue = object.Venue;
  P.Festival = object.Festival;
  P.id = object.id;
  contentList.push(P);
};


/*-----------------------------------------------------------------------------
tagbtn click event
-----------------------------------------------------------------------------*/
//create a click function this shoudl affect the output of content
$(".tagbtn").click(function(){
  var str = this.innerHTML;
  //if the button is already selected
  if($(this).hasClass("selected")){
    //remove the selected class so the button is no longer red
    $(this).removeClass("selected");
    document.getElementById("myDiv").appendChild(this);
    //you will also have to pop it off the list of selected tags
    //selectedList.pop(this.innerHTML);
    selectedList = jQuery.grep(selectedList, function( n ) {
      return ( n !== str);
    });
    if(selectedList == 0){
      hidden("selected-tags-container");
      //hidden("selected-tags-title");
    }
  }else{
    console.log(selectedList.length);
    if(selectedList == 0){
      visible("selected-tags-container");
      //visible("selected-tags-title")
    }
    //otherwise add the class name selected and add the tag to the selectedList
    $(this).addClass("selected");
    document.getElementById("selected-tags").appendChild(this);
    selectedList.push(this.innerHTML);
  }
  //after any button is pressed you want to update the content that is viewed using th eshow function found in (search.html)
  doCheck(selectedList);
  createFunction(0);
  createFunction(3);
  createFunction(6);
  createFunction(9);
});
/*-----------------------------------------------------------------------------
Window scroll event
-----------------------------------------------------------------------------*/
//when the user scrolls down the page we need to dynamicaly load data
$(window).on('scroll', function() {
  var screenSize = $(window).width();
  var screenH = $(window).height();
  var sb = document.getElementById("searchbtn");
  //console.log(sb.id);
  var y_scroll_pos = window.pageYOffset;
  //console.log(scroll_pos_test + ":declare");
  //console.log(screenH);
  //console.log(screenSize);
  if(y_scroll_pos > scroll_pos_test) {

    //console.log("load zone");
    createFunction(DisplayList);
    DisplayList = DisplayList + 3;
    if(screenSize <= 760){
      //the screen is small and the content is displayed one at at time
      //console.log(scroll_pos_test);
      scroll_pos_test =+ ((DisplayList/2 -1) * 398);

    }else if(screenSize > 760 && screenSize <= 985){
      //the screen size is medium and the content is displayed in pairs
      //console.log(DisplayList + " :medium");
      scroll_pos_test =+ (((DisplayList/4) - 2)*398);
    }else{
      //the content is displayed on a large screen and displayed 3 at a time
      //console.log(DisplayList + " :large");
      scroll_pos_test =+ (((DisplayList/6) - 3)*398);
    }
    //document.getElementById("tooltiptext").style.visibility = "visible";
  }
});

/*----------------------------------------------------------------------------
Clear all button click event
-----------------------------------------------------------------------------*/
//Below is a clear all function that is triggered when the button wiht the id "clearAll" is clicked
$("#clearAll").click(function(){
  //the function gets all the buttons in the tag list
  var tags = document.getElementsByClassName("tagbtn");
  //loops through them and sets there class - tagbtn gettting rid of any with the selector tag
  for(var i = 0; i < tags.length; i++){
    tags[i].className = "tagbtn";
    document.getElementById("myDiv").appendChild(tags[i]);
  }
  hidden("selected-tags-container");
  //hidden("selected-tags-title");
  //lastly we need to make sure that the selectedlist is empty
  selectedList = [];

  doCheck(selectedList);
});

/*-----------------------------------------------------------------------------
back to search click event
-----------------------------------------------------------------------------*/
$("#searchbtn").on("click", function() { $("body").scrollTop(0); });
