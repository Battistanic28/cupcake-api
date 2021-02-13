const BASE_URL = "http://127.0.0.1:5000/"

$('.delete').click(deleteCupcake)

async function deleteCupcake() {
    const id = $(this).data('id')
    await axios.delete(`/api/cupcakes/${id}`)
    $(this).parent().remove()
    alert('deleted')
}

$('#cupcake-form').on("submit", async function (e) {
    e.preventDefault();

    let flavor = $('#form-flavor').val();
    let size = $('#form-size').val();
    let rating = $('#form-rating').val();
    let image = $('#form-image').val();

    const newCupcake = await axios.post(`${BASE_URL}api/cupcakes`, {
        flavor,
        size,
        rating,
        image
    });
    return newCupcake
})