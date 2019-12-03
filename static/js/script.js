$(document).ready(() => { $("body").fadeIn("slow"); });

function MostrarLinks() {
    $(".menu").fadeOut("slow");
    setTimeout(() => { $("table").fadeIn("slow"); $("#Voltar").fadeIn("slow"); }, 1200);
}

function AddLinks() {
    $(".menu").fadeOut("slow");
    setTimeout(() => { $("#import").fadeIn("slow"); $("#Voltar").fadeIn("slow"); }, 1200);
}

function Voltar() {
    $("table").fadeOut("slow");
    $("#import").fadeOut("slow");
    $("#Voltar").fadeOut("slow");
    setTimeout(() => { $(".menu").fadeIn("slow") }, 1200);
}

function Enviar() {
    var nome = document.getElementById("#nome").value;
    console.log(nome);
}