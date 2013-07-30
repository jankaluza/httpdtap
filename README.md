httpdtap
========

Tool for querying httpd using SystemTap scripts.
- [Installation](#installation)
- [usage](#usage)
- Available commands:
   - [req_files](#httpdtap-req_files) - Shows files opened during the request.
   - [req_from](#httpdtap-req_from) - Shows requests received from particular IP.
   - [req_time](#httpdtap-req_time) - Shows requests sorted by the time needed to finished them.
   - [req_slower_than](#httpdtap-req_slower_than) - Shows requests slower than N ms.

## Installation

	git clone https://github.com/hanzz/httpdtap.git
	cd httpdtap
	sudo python setup.py install

## Usage

**Install http-debuginfo and kernel-debuginfo packages.** To Get the list of available commands, simply run:

	httpdtap

To execute chosen command, run:

	httpdtap req_from 127.0.0.1
	

For verbose mode add -v:

	httpdtap req_from 127.0.0.1 -v
	

## httpdtap req_files

Shows files opened during the request.

	$ httpdtap req_files
	[1374585172491278] [pid=6467, tid=6467] Handling new request: /wordpress/wp-includes/js/thickbox/thickbox.css?ver=20121105
	[1374585172491611] [pid=6109, tid=6109] Opened: /usr/share/wordpress/wp-admin/load-styles.php
	[1374585172491987] [pid=6467, tid=6467] Opened: /usr/share/wordpress/wp-includes/js/thickbox/thickbox.css
	[1374585172492053] [pid=6467, tid=6467] Request handled: /wordpress/wp-includes/js/thickbox/thickbox.css?ver=20121105

## httpdtap req_from

Shows requests received from particular IP.

	$ httpdtap req_from 127.0.0.1
	[1374585073614751] GET /wordpress/wp-admin/post-new.php HTTP/1.1
	[1374585073614751] Host: 127.0.0.1
	[1374585073614751] User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0
	[1374585073614751] Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
	[1374585073614751] Accept-Language: en-US,en;q=0.5
	[1374585073614751] Accept-Encoding: gzip, deflate
	[1374585073614751] Referer: http://127.0.0.1/wordpress/wp-admin/edit.php
	[1374585073614751] Cookie: wordpress_5bd7a9c61cda6e66fc921a05bc80ee93=admin%7C1374753628%7Cac915d5efaaff35c45c7d1432d95a57f; wordpress_test_cookie=WP+Cookie+check; wordpress_logged_in_5bd7a9c61cda6e66fc921a05bc80ee93=admin%7C1374753628%7Ceb7ba75e0a7c259fbfe470f111f42ac0; wp-settings-time-1=1374584745
	[1374585073614751] Connection: keep-alive
	[1374585073614751] Cache-Control: max-age=0
	[1374585073614751] ...
	[1374585074081221] POST /wordpress/wp-admin/admin-ajax.php HTTP/1.1
	[1374585074081221] Host: 127.0.0.1
	[1374585074081221] User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0
	[1374585074081221] Accept: */*
	[1374585074081221] Accept-Language: en-US,en;q=0.5
	[1374585074081221] Accept-Encoding: gzip, deflate
	[1374585074081221] Content-Type: application/x-www-form-urlencoded; charset=UTF-8
	[1374585074081221] X-Requested-With: XMLHttpRequest
	[1374585074081221] Referer: http://127.0.0.1/wordpress/wp-admin/post-new.php
	[1374585074081221] Content-Length: 56
	[1374585074081221] Cookie: wordpress_5bd7a9c61cda6e66fc921a05bc80ee93=admin%7C1374753628%7Cac915d5efaaff35c45c7d1432d95a57f; wordpress_test_cookie=WP+Cookie+check; wordpress_logged_in_5bd7a9c61cda6e66fc921a05bc80ee93=admin%7C1374753628%7Ceb7ba75e0a7c259fbfe470f111f42ac0; wp-settings-time-1=1374585074
	[1374585074081221] Connection: keep-alive
	[1374585074081221] Pragma: no-cache
	[1374585074081221] Cache-Control: no-cache
	[1374585074081221] ...

## httpdtap req_time

Shows requests sorted by the time needed to finished them.

	$ httpdtap req_time
	<ctrl+c>
	10 slowest requests:
	1. '/wordpress/wp-admin/plugin-install.php?tab=search&type=tag&s=AJAX': 2501549 us
	2. '/wordpress/wp-admin/plugins.php': 921770 us
	3. '/wordpress/wp-admin/post-new.php': 397853 us
	4. '/wordpress/wp-admin/index.php': 328047 us
	5. '/wordpress/wp-admin/edit.php': 179953 us
	6. '/wordpress/wp-admin/plugin-install.php': 170893 us
	7. '/wordpress/wp-admin/users.php': 170017 us
	8. '/wordpress/wp-admin/tools.php': 166010 us
	9. '/wordpress/wp-includes/js/tinymce/wp-tinymce.php?c=1&ver=358-24486': 111378 us
	10. '/wordpress/wp-includes/js/tinymce/plugins/inlinepopups/skins/clearlooks2/window.css?ver=358-24486': 89904 us
	Grouped requests by URI:
	1. '/wordpress/wp-admin/plugin-install.php?tab=search&type=tag&s=AJAX': avg=2501549 us, min=2501549 us, max=2501549 us
	2. '/wordpress/wp-admin/plugins.php': avg=921770 us, min=921770 us, max=921770 us
	3. '/wordpress/wp-admin/post-new.php': avg=397853 us, min=397853 us, max=397853 us
	4. '/wordpress/wp-admin/index.php': avg=328047 us, min=328047 us, max=328047 us
	5. '/wordpress/wp-admin/edit.php': avg=179953 us, min=179953 us, max=179953 us
	6. '/wordpress/wp-admin/plugin-install.php': avg=170893 us, min=170893 us, max=170893 us
	7. '/wordpress/wp-admin/users.php': avg=170017 us, min=170017 us, max=170017 us
	8. '/wordpress/wp-admin/tools.php': avg=166010 us, min=166010 us, max=166010 us
	9. '/wordpress/wp-includes/js/tinymce/wp-tinymce.php?c=1&ver=358-24486': avg=111378 us, min=111378 us, max=111378 us
	10. '/wordpress/wp-includes/js/tinymce/plugins/inlinepopups/skins/clearlooks2/window.css?ver=358-24486': avg=89904 us, min=89904 us, max=89904 us
	11. '/wordpress/wp-admin/load-scripts.php?c=1&load%5B%5D=admin-bar,hoverIntent,common,schedule,wp-ajax-response,autosave,suggest,jquery-color,wp-lists,jquery-ui-core,jquery-ui-widget,jq&load%5B%5D=uery-ui-mouse,jquery-ui-sortable,postbox,post,thickbox,underscore,shortcode,backbone,media-models,wp-plupload,media-views,media-&load%5B%5D=editor,word-count,editor,quicktags,jquery-ui-resizable,jquery-ui-draggable,jquery-ui-button,jquery-ui-position,jquery-ui-dialog,&load%5B%5D=wpdialogs,wplink,wpdialogs-popup,wp-ful': avg=78731 us, min=78731 us, max=78731 us
	12. '/wordpress/wp-includes/js/tinymce/themes/advanced/skins/wp_theme/content.css': avg=76155 us, min=76155 us, max=76155 us
	13. '/wordpress/wp-content/themes/twentytwelve/editor-style.css': avg=29832 us, min=29832 us, max=29832 us
	14. '/wordpress/wp-includes/js/tinymce/langs/wp-langs-en.js?ver=358-24486': avg=29542 us, min=29542 us, max=29542 us
	15. '/wordpress/wp-includes/js/tinymce/plugins/wpgallery/img/edit.png': avg=20388 us, min=20388 us, max=20388 us
	16. '/wordpress/wp-includes/js/tinymce/plugins/wpgallery/img/delete.png': avg=20165 us, min=20165 us, max=20165 us
	17. '/wordpress/wp-admin/load-scripts.php?c=1&load%5B%5D=admin-bar,hoverIntent,common,wp-ajax-response,jquery-color,wp-lists,quicktags,jquery-query,admin-comments,jquery-ui-core,jquery-&load%5B%5D=ui-widget,jquery-ui-mouse,jquery-ui-sortable,postbox,dashboard,customize-base,customize-loader,thickbox,plugin-install,underscor&load%5B%5D=e,shortcode,media-upload,backbone,media-models,plupload,plupload-html5,plupload-flash,plupload-silverlight,plupload-html4,wp-plu&load%5B%5D=pload,media-views,media-editor,word-cou': avg=17788 us, min=17788 us, max=17788 us
	18. '/wordpress/wp-includes/images/wpicons.png?ver=20120720': avg=16016 us, min=16016 us, max=16016 us
	19. '/wordpress/wp-includes/js/tinymce/plugins/spellchecker/css/content.css': avg=11515 us, min=11515 us, max=11515 us
	20. '/wordpress/wp-admin/load-styles.php?c=1&dir=ltr&load=admin-bar,buttons,media-views,wp-admin&ver=3.5.2': avg=11324 us, min=11324 us, max=11324 us
	21. '/wordpress/wp-includes/js/tinymce/plugins/wpeditimage/img/image.png': avg=11178 us, min=11178 us, max=11178 us
	22. '/wordpress/wp-includes/js/tinymce/plugins/wpeditimage/img/delete.png': avg=10861 us, min=10861 us, max=10861 us
	23. '/wordpress/wp-admin/load-scripts.php?c=1&load%5B%5D=jquery,utils,plupload,plupload-html5,plupload-flash,plupload-silverlight,plupload-html4,json2&ver=3.5.2': avg=10533 us, min=10533 us, max=10533 us
	24. '/wordpress/wp-admin/load-styles.php?c=1&dir=ltr&load=media-views,wp-jquery-ui-dialog&ver=3.5.2': avg=7051 us, min=7051 us, max=7051 us
	25. '/wordpress/wp-admin/images/stars.png?ver=20121108': avg=684 us, min=684 us, max=684 us
	26. '/wordpress/wp-includes/js/thickbox/thickbox.css?ver=20121105': avg=248 us, min=160 us, max=503 us
	27. '/wordpress/wp-admin/images/press-this.png?v=20120502': avg=194 us, min=194 us, max=194 us
	28. '/wordpress/wp-admin/images/date-button.gif': avg=174 us, min=174 us, max=174 us
	29. '/wordpress/wp-admin/css/colors-fresh.min.css?ver=3.5.2': avg=163 us, min=90 us, max=234 us
	30. '/wordpress/wp-includes/css/editor.min.css?ver=3.5.2': avg=161 us, min=154 us, max=168 us
	31. '/wordpress/wp-includes/images/down_arrow.gif': avg=72 us, min=72 us, max=72 us
	32. '/wordpress/wp-admin/images/resize.gif': avg=72 us, min=72 us, max=72 us

## httpdtap req_slower_than

Shows requests slower than N ms.

	$ httpdtap req_slower_than 1 with_download
	Showing requests slower than 1 ms
	Slow request took 5273 ms: GET /test.img HTTP/1.1
