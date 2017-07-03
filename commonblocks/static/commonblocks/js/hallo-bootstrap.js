'use strict';

function makeHalloSimpleRichTextEditable(id, plugins) {
    if ($.isPlainObject(plugins)) {
        var defaultPlugins = $.extend(true, {}, window.halloPlugins);

        $.each(plugins, function(plugin, options) {
            window.registerHalloPlugin(plugin, options);
        });

        window.makeHalloRichTextEditable(id);

        window.halloPlugins = $.extend(true, {}, defaultPlugins);
    }
};

window.makeHalloSimpleRichTextEditable = makeHalloSimpleRichTextEditable;
