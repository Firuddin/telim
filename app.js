let editor = document.getElementById("editor")

function BoldText() {
    document.execCommand("bold",false,"")
}

function ItalicText() {
    document.execCommand("italic",false,"")
}

function UnderLineText() {
    document.execCommand("underline",false,"")
}
function Undo() {
    document.execCommand("undo")
}
function Redo() {
    document.execCommand("redo")
}

function FontSize() {
    let FontSize = document.getElementById("ChangeFontSize").value;
    document.execCommand("fontSize",false,FontSize)
}


function FontChange() {
    let Font = document.getElementById("ChangeFont").value;
    document.execCommand("fontName",false,Font)
}

function CutText() {
    let selection = window.getSelection();
    let range = document.createRange();
    range.selectNodeContents(editor)
    selection.removeAllRanges()
    selection.addRange(range)
    document.execCommand('cut')
}

function CopyText() {
    let selection = window.getSelection();
    let range = document.createRange();
    range.selectNodeContents(editor)
    selection.removeAllRanges()
    selection.addRange(range)
    document.execCommand('copy')
}

function PasteText() {
    navigator.clipboard.readText().then((clipText)=>{
        document.execCommand("insertText",false,clipText)
    })
}