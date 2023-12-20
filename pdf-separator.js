"use strict";

const fs = require("fs");
const { PDFDocument } = require("pdf-lib");
const { join } = require("path");
const pdf = require("pdf-parse");
const { readFile } = require("fs/promises");

async function separarPaginasPDF() {
  const antes = Date.now();

  // Carregue o arquivo PDF original
  const pdfData = await fs.promises.readFile("Total.pdf");
  const pdfDoc = await PDFDocument.load(pdfData);

  // Crie um novo documento PDF para cada página separada
  let total = pdfDoc.getPageCount() > 5 ? 1 : pdfDoc.getPageCount();
  let fileName = "";
  for (let i = 0; i < total; i++) {
    const newPdfDoc = await PDFDocument.create();
    const [page] = await newPdfDoc.copyPages(pdfDoc, [i]);
    newPdfDoc.addPage(page);

    // Salve o novo documento em um arquivo separado
     const pdfBytes = await newPdfDoc.save();

   // fileName = `holerites/pagina_${i + 1}.pdf`;
   // await fs.promises.writeFile(fileName, pdfBytes);
   // await renomearPaginaPDF(fileName).catch((error) => {
    //  console.error("Ocorreu um erro:", error);
   // });
  }

  console.log("Páginas separadas com sucesso!");
  const duracao = Date.now() - antes;
  console.log("levou " + duracao + "ms");
}

async function renomearPaginaPDF(file) {
  const numberPattern = /\d+/g;
  const basePath = __dirname;
  const pathDestination = join(basePath, "holerites");
  const dataBuffer = await readFile(join(basePath, file));
  const data = await pdf(dataBuffer);
  const text = data.text.split("\n");
  const matricula = text[8].match(numberPattern).join([]);
  const novoNomeArquivo = `${matricula}-holerite.pdf`;

  // Carregue o arquivo PDF original
  const pdfData = await fs.promises.readFile(file);
  const pdfDoc = await PDFDocument.load(pdfData);
KT
  // Salve o arquivo PDF com o novo nome
  await pdfDoc.save();
  await fs.promises.rename(
    join(basePath, file),
    join(pathDestination, novoNomeArquivo)
  );

  console.log(`Página renomeada para: ${novoNomeArquivo}`);
}

separarPaginasPDF().catch((error) => {
  console.error("Ocorreu um erro:", error);
});
