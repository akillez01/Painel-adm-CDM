$(document).ready(function() {
  $('#changelist-filter').prepend(`
    <div class="export-section">
      <h2>Exportar</h2>
      <ul>
        <li><a href="/produto/export/csv/" class="export-link">CSV</a></li>
        <li><a href="/produto/export/xlsx/" class="export-link">XLSX</a></li>
      </ul>
    </div>
  `);
  $('.object-tools').prepend(`
    <div class="import-section">
      <li><a href="/produto/import/csv/" class="import-link">Importar CSV</a></li>
      <li><a href="/produto/import/xlsx/" class="import-link">Importar XLSX</a></li>
    </div>
  `);
});