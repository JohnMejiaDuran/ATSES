
const btnAbrirModal = document.querySelector("#btn-abrir-modal");
const btnCerrarModal =document.querySelector("#btn-cerrar-modal");
const modal = document.querySelector("#modal");

btnAbrirModal.addEventListener("click",()=>{
    modal.showModal()
})
btnCerrarModal.addEventListener("click", () => {
    modal.close(); // Cierra el modal al hacer clic en el botón de cierre
});


const btnAbrirModal_usuarios = document.querySelector("#btn-abrir-modal");
const btnCerrarModal_usuarios =document.querySelector("#btn-cerrar-modal");
const modal_usuarios = document.querySelector("#modal_usuarios");

btnAbrirModal.addEventListener("click",()=>{
    modal_usuarios.showModal()
})
btnCerrarModal.addEventListener("click", () => {
    modal_usuarios.close(); // Cierra el modal al hacer clic en el botón de cierre
});
