function onPastePhone(event) {
    let paste = event.originalEvent.clipboardData.getData('text');
    event.target.value = String(paste).replace(/[^0-9]/g, '')
        .replace(/(\d)(\d{3})(\d{3})(\d{2})(\d{2})/, '$2$3$4$5');
    event.target.dispatchEvent(new Event('input', {bubbles: true}))
}

$(function () {
    $('input[data-phone="yes"]').on('paste', onPastePhone)
})