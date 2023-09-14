
const btnAbrirModal = document.querySelector("#btn-abrir-modal");
const btnCerrarModal =document.querySelector("#btn-cerrar-modal");
const modal = document.querySelector("#modal");

btnAbrirModal.addEventListener("click",()=>{
    modal.showModal()
})
btnCerrarModal.addEventListener("click", () => {
    modal.close(); // Cierra el modal al hacer clic en el botón de cierre
});

console.log("El código se está ejecutando correctamente.");
