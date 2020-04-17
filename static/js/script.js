$(document).ready(() => { // inicializa as animações de inicialização
	setTimeout(() => { $("#barra").fadeIn("slow"); }, 1200);
	setTimeout(() => { $("#mostrar").fadeIn("slow"); }, 2300);
	$(".menu").addClass("transicao");
	// $(".tabela").css("width", (window.screen.availWidth - 10) + "px");
	// $(".tabela").css("height", "400px");
	$(".tabela").css("overflow", "auto");
});

function MostrarLinks() { // executa a animação da tela de links
	// var tamTela = ;
	// var tamTela = $(document).height();
	$(".tabela").css("height", (window.screen.availHeight / 2) + "px");
	$(".menu").fadeOut("slow").removeClass("transicao");
	setTimeout(() => { $(".tabela").fadeIn("slow"); $("#Voltar").fadeIn("slow"); }, 1200);
	setTimeout(() => { $("td").addClass("transicao"); }, 1500);
}

function AddLinks() { // executa animação do adicionar os links
	$(".menu").fadeOut("slow").removeClass("transicao");
	setTimeout(() => { $("#import").fadeIn("slow"); $("#Voltar").fadeIn("slow"); }, 1200);
}

function Voltar() { // executa a animação de voltar a pagina inicial
	$("td").removeClass("transicao");
	$(".tabela").fadeOut("slow");
	$("#import").fadeOut("slow");
	$("#Voltar").fadeOut("slow");
	setTimeout(() => { $(".menu").fadeIn("slow"); }, 1200);
	setTimeout(() => { $(".menu").addClass("transicao"); }, 1500);
}

function Limpar(id) { // limpa as caixas de texto
	document.getElementById(id).value = "";
	// alert("Maluco");
}