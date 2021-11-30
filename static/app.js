// function to show display form 
function showAndHideForm () {
    $(".new_cake").show()
    $('.add_new_cake').hide()
}   

// cancel new cake and hide form
function cancelNewCake() {
    $(".new_cake").hide()
       $('.add_new_cake').show()
}

$('.add_new_cake').click(showAndHideForm)
$(".cancel_new_cake").click(cancelNewCake)

async function getCupCakes() {
    const response = await axios.get('/api/cupcakes')

    for (cake of response.data.cupcakes) {
        $(".cake_list").append(`<li> Flavor: ${cake.flavor}, 
        size: ${cake.size}, Rating: ${cake.rating} </li>`)
    }
}

// submit form to create new cupcake
$(".new_cake_form").click(function (e) {
})


//  get cupcakes when pages loads and display on page.
getCupCakes()
