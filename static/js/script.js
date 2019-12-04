$(document).ready(() => { 
	setTimeout(() => { $("#barra").fadeIn("slow"); }, 1200);
	setTimeout(() => { $("#mostrar").fadeIn("slow"); }, 2300);
	$(".menu").addClass("transicao");
});

function MostrarLinks() {
	$(".menu").fadeOut("slow").removeClass("transicao");
	setTimeout(() => { $("table").fadeIn("slow"); $("#Voltar").fadeIn("slow"); }, 1200);
}

function AddLinks() {
	$(".menu").fadeOut("slow").removeClass("transicao");
	setTimeout(() => { $("#import").fadeIn("slow"); $("#Voltar").fadeIn("slow"); }, 1200);
}

function Voltar() {
	$("table").fadeOut("slow");
	$("#import").fadeOut("slow");
	$("#Voltar").fadeOut("slow");
	setTimeout(() => { $(".menu").fadeIn("slow"); }, 1200);
	setTimeout(() => { $(".menu").addClass("transicao"); }, 1500);
}

function Enviar() {
	var nome = document.getElementById("#nome").value;
	console.log(nome);
}