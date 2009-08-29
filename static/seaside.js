var seaside = function() {
  var editor_config = {
    height: '500px',
    width: '600px',
    handleSubmit: true
  };
  
  return {
    confirm_delete : function() {
      var forms = document.getElementsByTagName('form');
      YAHOO.util.Event.on(forms, 'submit', function(e) {
        if(!confirm('Are you sure want to delete this item?')) {
          YAHOO.util.Event.preventDefault(e);
        }
      });
    },
    render_yui_editor : function(textarea) {
      var editor = new YAHOO.widget.Editor(textarea, editor_config);
      editor.render();
    }
  };
}();