'use strict';

/**
 * registerHalloPlugin() applies to all editor instances of a Page.
 * We want to encapsulate custom plugin configuration, per field.
 */
function makeHalloSimpleRichTextEditable(id, plugins) {
    var defaultPlugins = $.extend({}, halloPlugins);

    if (typeof plugins === 'object') {
        $.each(plugins, function(plugin, options) {
            registerHalloPlugin(plugin, options);
        });

        makeHalloRichTextEditable(id);
    }

    halloPlugins = $.extend({}, defaultPlugins);
};