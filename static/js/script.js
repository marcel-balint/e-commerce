$(document).ready(function() {

 var productForm = $(".form-product-ajax")

 productForm.submit(function(event) {
  event.preventDefault();

  var thisForm = $(this)
  var actionEndpoint = thisForm.attr("action");
  var httpMethod = thisForm.attr("method");
  var formData = thisForm.serialize();
  $.ajax({
   url: actionEndpoint,
   method: httpMethod,
   data: formData,
   success: function(data) {

    var submitSpan = thisForm.find(".submit-span")
    if (data.added) {
     submitSpan.html("In cart <button type='submit' class='btn remove'>Remove?</button>")
    }
    else {
     submitSpan.html("<button type='submit'  class='btn btn-success add-to-cart'>Add to cart</button>")
    }
    var navbarCount = $(".navbar-cart-count")
    navbarCount.text(data.cartItemCount)
   },
   error: function(errorData) {
    console.log("error")
    console.log(errorData)
   }
  })
 })

})
