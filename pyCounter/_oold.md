2019-10-25T13:36:30+02:00
Scanning C:\Users\marti\Documents\gambio_tickets75
Including file extensions: php
Processed 983939 lines contained in 5839 files.
Processing took 1056.7554819584 seconds.

# critical
#### C:\Users\marti\Documents\gambio_tickets75\PdfCreator\font\makefont\makefont.php
* deprecatedFunctions
 * Line 291: `	set_magic_quotes_runtime(0);`

#### C:\Users\marti\Documents\gambio_tickets75\PdfCreator\fpdf.php
* oldClassConstructors
 * Line 75: `function FPDF($orientation='P',$unit='mm',$format='A4')`
* deprecatedFunctions
 * Line 865: `		$mqr=get_magic_quotes_runtime();`
 * Line 866: `		set_magic_quotes_runtime(0);`
 * Line 898: `		set_magic_quotes_runtime($mqr);`
 * Line 1183: `	$mqr=get_magic_quotes_runtime();`
 * Line 1184: `	set_magic_quotes_runtime(0);`
 * Line 1222: `	set_magic_quotes_runtime($mqr);`

#### C:\Users\marti\Documents\gambio_tickets75\PdfCreator\gif.php
* oldClassConstructors
 * Line 101: `	function CGIFLZW()`
 * Line 271: `	function CGIFCOLORTABLE()`
 * Line 352: `	function CGIFFILEHEADER()`
 * Line 415: `	function CGIFIMAGEHEADER()`
 * Line 472: `	function CGIFIMAGE()`
 * Line 609: `	function CGIF()`

#### C:\Users\marti\Documents\gambio_tickets75\StyleEdit\classes\GMBoxesMaster.php
* oldClassConstructors
 * Line 15: `    function GMBoxesMaster($p_v_current_template) `
* deprecatedFunctions
 * Line 21: `    	mysql_query('`
 * Line 38: `						template_name = '" . mysql_real_escape_string($this->v_current_template) . "' AND`
 * Line 42: `		$t_result = mysql_query($t_sql);`
 * Line 43: `		if(mysql_num_rows($t_result) > 0)`
 * Line 46: `			while($t_result_array = mysql_fetch_array($t_result))`
 * Line 48: `				mysql_query("UPDATE gm_boxes`
 * Line 51: `									template_name = '" . mysql_real_escape_string($this->v_current_template) . "' AND`
 * Line 52: `									box_name = '" . mysql_real_escape_string($t_result_array['box_name']) . "'");`
 * Line 60: `						template_name = '" . mysql_real_escape_string($this->v_current_template) . "' AND`
 * Line 64: `		$t_result = mysql_query($t_sql);`
 * Line 65: `		if(mysql_num_rows($t_result) > 0)`
 * Line 68: `			while($t_result_array = mysql_fetch_array($t_result))`
 * Line 70: `				mysql_query("UPDATE gm_boxes`
 * Line 73: `									template_name = '" . mysql_real_escape_string($this->v_current_template) . "' AND`
 * Line 74: `									box_name = '" . mysql_real_escape_string($t_result_array['box_name']) . "'");`
 * Line 82: `    	$result = mysql_query('`
 * Line 92: `    	$data = mysql_fetch_array($result);`
 * Line 98: `    	$result = mysql_query('`
 * Line 114: `    	$result = mysql_query('`
 * Line 125: `    	while(($row = mysql_fetch_array($result) ))`
 * Line 143: `    	$result = mysql_query('`
 * Line 153: `    	$data = mysql_fetch_array($result);`
 * Line 175: `		$t_query = mysql_query("`
 * Line 187: `		if((int)mysql_num_rows($t_query) > 0)`
 * Line 189: `			$t_row = mysql_fetch_array($t_query, MYSQL_ASSOC);`
 * Line 200: `		$t_query = mysql_query("`
 * Line 212: `		$t_query = mysql_query("`
 * Line 225: `		$t_query = mysql_query("`
 * Line 236: `		$t_query = mysql_query("`
 * Line 246: `		if((int)mysql_num_rows($t_query) > 0)`
 * Line 258: `		$t_query = mysql_query("`
 * Line 268: `		if((int)mysql_num_rows($t_query) > 0)`
 * Line 276: `					$t_query = mysql_query("`

#### C:\Users\marti\Documents\gambio_tickets75\StyleEdit\classes\GMCSS.php
* oldClassConstructors
 * Line 55: `		function GMCSS($p_css_file, $p_type='archive')`
 * Line 384: `		function GMCSSImport($p_css_file = false, $p_import_mode = '')`
 * Line 791: `		function GMCSSExport($p_css_file)`
 * Line 912: `		function GMCSSUpload($p_files, $p_type)`
 * Line 982: `		function GMCSSArchive()`
* deprecatedFunctions
 * Line 302: `			$t_css_query = mysql_query("`
 * Line 311: `			if((int)mysql_num_rows($t_css_query) > 0)`
 * Line 313: `				$t_row_styles				= mysql_fetch_array($t_css_query, MYSQL_ASSOC);`
 * Line 316: `			$t_css_query = mysql_query("`
 * Line 325: `			if((int)mysql_num_rows($t_css_query) > 0)`
 * Line 327: `				$t_row_styles						= mysql_fetch_array($t_css_query, MYSQL_ASSOC);`
 * Line 476: `			$t_query = mysql_query("`
 * Line 487: `			if((int)mysql_num_rows($t_query) > 0)`
 * Line 489: `				while($t_row = mysql_fetch_array($t_query))`
 * Line 491: `					mysql_query("`
 * Line 501: `						mysql_query("`
 * Line 549: `			mysql_query("`
 * Line 656: `					mysql_query("`
 * Line 668: `					mysql_query("`
 * Line 692: `			mysql_query("`
 * Line 711: `			mysql_query("`
 * Line 719: `			return mysql_insert_id();`
 * Line 729: `			$t_query = mysql_query("`
 * Line 739: `			if((int)mysql_num_rows($t_query) > 0)`
 * Line 741: `				$t_row = mysql_fetch_array($t_query);`
 * Line 757: `			$t_query = mysql_query("`
 * Line 767: `			if((int)mysql_num_rows($t_query) > 0)`
 * Line 769: `				$t_row = mysql_fetch_array($t_query);`
 * Line 853: `			$t_css_query = mysql_query("`
 * Line 865: `			while($t_css_selector = mysql_fetch_array($t_css_query))`
 * Line 870: `				$t_css_atr_query = mysql_query('`
 * Line 883: `				while(($t_css_atr = mysql_fetch_array($t_css_atr_query)))`

#### C:\Users\marti\Documents\gambio_tickets75\StyleEdit\classes\GMCSSManager.php
* oldClassConstructors
 * Line 74: `		function GMCSSManager($p_token = '')`
* deprecatedFunctions
 * Line 97: `					$t_query = mysql_query("`
 * Line 108: `					if((int)mysql_num_rows($t_query) > 0)`
 * Line 122: `						$t_row = mysql_fetch_array($t_query, MYSQL_ASSOC);`
 * Line 124: `						mysql_query("`
 * Line 149: `						&& (int)mysql_num_rows($t_query) == 0`
 * Line 152: `						mysql_query("`
 * Line 194: `			mysql_query("`
 * Line 216: `			$t_query = mysql_query("`
 * Line 232: `			if((int)mysql_num_rows($t_query) > 0)`
 * Line 239: `				while($t_row = mysql_fetch_array($t_query, MYSQL_ASSOC))`
 * Line 298: `			$t_query = mysql_query("`
 * Line 314: `			while(($t_row = mysql_fetch_array($t_query, MYSQL_ASSOC))) `
 * Line 316: `				$t_query_contents = mysql_query("`
 * Line 334: `				if((int)mysql_num_rows($t_query_contents) > 0)`
 * Line 336: `					while($t_row_contents = mysql_fetch_array($t_query_contents, MYSQL_ASSOC))`
 * Line 360: `			$t_query = mysql_query("`
 * Line 369: `			if((int)mysql_num_rows($t_query) > 0)`
 * Line 371: `				$t_row = mysql_fetch_array($t_query, MYSQL_ASSOC);`
 * Line 386: `			$t_query = mysql_query("`
 * Line 397: `			if((int)mysql_num_rows($t_query) > 0)`
 * Line 399: `				$t_row = mysql_fetch_array($t_query, MYSQL_ASSOC);`
 * Line 415: `			$t_query = mysql_query("`
 * Line 426: `			if((int)mysql_num_rows($t_query) > 0)`
 * Line 437: `				while($t_row = mysql_fetch_array($t_query, MYSQL_ASSOC))`
 * Line 510: `			$t_query = mysql_query("`
 * Line 518: `			if((int)mysql_num_rows($t_query) > 0)`
 * Line 521: `				while($t_row = mysql_fetch_array($t_query, MYSQL_ASSOC))`
 * Line 599: `				$t_query = mysql_query("`
 * Line 613: `				$t_query = mysql_query("`
 * Line 625: `			if((int)mysql_num_rows($t_query) > 0)`
 * Line 627: `				$t_row		= mysql_fetch_array($t_query, MYSQL_ASSOC);`
 * Line 658: `			$t_query = mysql_query("`
 * Line 668: `			if(mysql_num_rows($t_query) > 0)`
 * Line 670: `				while($t_row = mysql_fetch_array($t_query, MYSQL_ASSOC))`
 * Line 672: `					$t_file_query = mysql_query("`
 * Line 683: `					if(mysql_num_rows($t_file_query) > 0)`
 * Line 685: `						mysql_query("`
 * Line 695: `						$t_file_row				= mysql_fetch_array($t_file_query, MYSQL_ASSOC);`
 * Line 716: `				mysql_query("`
 * Line 727: `				$t_query = mysql_query("`
 * Line 737: `				if(mysql_num_rows($t_query) > 0)`
 * Line 739: `					while($t_row = mysql_fetch_array($t_query, MYSQL_ASSOC))`
 * Line 741: `						mysql_query("`
 * Line 795: `			mysql_query("`
 * Line 804: `			mysql_query("`
 * Line 815: `			$t_query = mysql_query("`
 * Line 826: `			$t_row = mysql_fetch_array($t_query);`
 * Line 836: `					mysql_query("`
 * Line 855: `			$t_query_history =  mysql_query("`
 * Line 866: `			if(mysql_num_rows($t_query_history) > 0)`
 * Line 868: `				while($t_row_history = mysql_fetch_array($t_query_history, MYSQL_ASSOC))`
 * Line 871: `					$t_query = mysql_query("`
 * Line 885: `					if(mysql_num_rows($t_query) > 0)`
 * Line 887: `						while($t_row = mysql_fetch_array($t_query, MYSQL_ASSOC))`
 * Line 896: `					mysql_query("`
 * Line 903: `					mysql_query("`
 * Line 952: `			$t_query = mysql_query("	SELECT`
 * Line 966: `			if(mysql_num_rows($t_query) > 0)`
 * Line 968: `				$t_history			= mysql_fetch_array($t_query);`
 * Line 972: `				$t_query = mysql_query("	SELECT`
 * Line 980: `				if(mysql_num_rows($t_query) > 0)`
 * Line 982: `					while($t_row = mysql_fetch_array($t_query, MYSQL_ASSOC))`
 * Line 989: `					mysql_query("`
 * Line 998: `					mysql_query("`
 * Line 1031: `			$t_query = mysql_query("`
 * Line 1044: `			if(mysql_num_rows($t_query) > 0)`
 * Line 1046: `				$t_count = mysql_fetch_array($t_query, MYSQL_ASSOC);`
 * Line 1060: `			$t_query = mysql_query("`
 * Line 1073: `			if(mysql_num_rows($t_query) > 0)`
 * Line 1075: `				$t_history_id = mysql_fetch_array($t_query, MYSQL_ASSOC);`

#### C:\Users\marti\Documents\gambio_tickets75\StyleEdit\classes\GMSEAjax.php
* oldClassConstructors
 * Line 26: `		function GMSEAjax($p_param)`

#### C:\Users\marti\Documents\gambio_tickets75\StyleEdit\classes\GMSEError.php
* oldClassConstructors
 * Line 17: `		function GMSEError()`

#### C:\Users\marti\Documents\gambio_tickets75\StyleEdit\classes\GMSESecurity.php
* oldClassConstructors
 * Line 14: `		function GMSESecurity()`
* deprecatedFunctions
 * Line 30: `					mysql_query("`
 * Line 49: `			mysql_query("`
 * Line 67: `				$t_query =  mysql_query("`
 * Line 79: `				$t_query	=  mysql_query("`
 * Line 88: `			if(mysql_num_rows($t_query) > 0)`
 * Line 90: `				while($t_row = mysql_fetch_array($t_query, MYSQL_ASSOC))`
 * Line 92: `					$t_query_history =  mysql_query("`
 * Line 101: `					if(mysql_num_rows($t_query_history) > 0)`
 * Line 103: `						while($t_row_history = mysql_fetch_array($t_query_history, MYSQL_ASSOC))`
 * Line 105: `							mysql_query("`
 * Line 113: `						mysql_query("`
 * Line 123: `						mysql_query("`
 * Line 143: `			$t_query =  mysql_query("`
 * Line 153: `			if(mysql_num_rows($t_query) > 0)`
 * Line 155: `				$t_row = mysql_fetch_array($t_query, MYSQL_ASSOC);`
 * Line 188: `			$t_query =  mysql_query("`
 * Line 196: `			if(mysql_num_rows($t_query) > 0)`
 * Line 198: `				$t_token_id = mysql_fetch_array($t_query);`

#### C:\Users\marti\Documents\gambio_tickets75\StyleEdit\style_edit_request.php
* deprecatedFunctions
 * Line 33: `	mysql_connect(SE_CFG_SERVER, SE_CFG_USERNAME, SE_CFG_PASSWORD);`
 * Line 34: `	mysql_select_db(SE_CFG_DATABASE);`
 * Line 51: `	mysql_close();`

#### C:\Users\marti\Documents\gambio_tickets75\admin\accounting.php
* deprecatedFunctions
 * Line 24: `       $fields = mysql_list_fields(DB_DATABASE, TABLE_ADMIN_ACCESS);`
 * Line 25: `       $columns = mysql_num_fields($fields);`
 * Line 27: `             $field=mysql_field_name($fields, $i);`
 * Line 131: `$fields = mysql_list_fields(DB_DATABASE, TABLE_ADMIN_ACCESS);`
 * Line 132: `$columns = mysql_num_fields($fields);`
 * Line 134: `    $field=mysql_field_name($fields, $i);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\brickfox.php
* oldClassConstructors
 * Line 26: `	function Brickfox()`

#### C:\Users\marti\Documents\gambio_tickets75\admin\clear_cache.php
* deprecatedFunctions
 * Line 78: `												while(($t_row = mysql_fetch_array($t_result) ))`

#### C:\Users\marti\Documents\gambio_tickets75\admin\csv_backend.php
* deprecatedFunctions
 * Line 29: `				// mysql_query() to avoid warning messages if table does not exist`
 * Line 30: `				@mysql_query("TRUNCATE personal_offers_by_customers_status_");`
 * Line 31: `				@mysql_query("TRUNCATE personal_offers_by_customers_status_1");`
 * Line 32: `				@mysql_query("TRUNCATE personal_offers_by_customers_status_2");`
 * Line 33: `				@mysql_query("TRUNCATE personal_offers_by_customers_status_3");`
 * Line 34: `				@mysql_query("TRUNCATE personal_offers_by_customers_status_4");`
 * Line 35: `				@mysql_query("TRUNCATE personal_offers_by_customers_status_5");`
 * Line 36: `				@mysql_query("TRUNCATE personal_offers_by_customers_status_6");`
 * Line 37: `				@mysql_query("TRUNCATE personal_offers_by_customers_status_7");`
 * Line 38: `				@mysql_query("TRUNCATE personal_offers_by_customers_status_8");`
 * Line 39: `				@mysql_query("TRUNCATE personal_offers_by_customers_status_9");`
 * Line 40: `				@mysql_query("TRUNCATE personal_offers_by_customers_status_10");`
 * Line 75: `			@mysql_query("OPTIMIZE TABLE personal_offers_by_customers_status_");`
 * Line 76: `			@mysql_query("OPTIMIZE TABLE personal_offers_by_customers_status_1");`
 * Line 77: `			@mysql_query("OPTIMIZE TABLE personal_offers_by_customers_status_2");`
 * Line 78: `			@mysql_query("OPTIMIZE TABLE personal_offers_by_customers_status_3");`
 * Line 79: `			@mysql_query("OPTIMIZE TABLE personal_offers_by_customers_status_4");`
 * Line 80: `			@mysql_query("OPTIMIZE TABLE personal_offers_by_customers_status_5");`
 * Line 81: `			@mysql_query("OPTIMIZE TABLE personal_offers_by_customers_status_6");`
 * Line 82: `			@mysql_query("OPTIMIZE TABLE personal_offers_by_customers_status_7");`
 * Line 83: `			@mysql_query("OPTIMIZE TABLE personal_offers_by_customers_status_8");`
 * Line 84: `			@mysql_query("OPTIMIZE TABLE personal_offers_by_customers_status_9");`
 * Line 85: `			@mysql_query("OPTIMIZE TABLE personal_offers_by_customers_status_10");`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\GMAltText.php
* oldClassConstructors
 * Line 14: `		function GMAltText() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\GMGroupIdChecker.php
* oldClassConstructors
 * Line 26: `		function GMGroupIdChecker($p_languages_id)`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\GMIdStarts.php
* oldClassConstructors
 * Line 15: `		function GMIdStarts() {`
* deprecatedFunctions
 * Line 25: `			if(mysql_num_rows($get_orders_id) == 1){`
 * Line 39: `			if(mysql_num_rows($get_customers_id) == 1){`
 * Line 53: `			if(mysql_num_rows($get_current_autoindex) == 1){`
 * Line 67: `			if(mysql_num_rows($get_current_autoindex) == 1){`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\GMInvoicing.php
* oldClassConstructors
 * Line 75: `		function GMInvoicing()`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\GMInvoicingConfiguration.php
* oldClassConstructors
 * Line 40: `		function GMInvoicingConfiguration()`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\GMLangFileImport.php
* oldClassConstructors
 * Line 14: `	function GMLangFileImport() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\GMModulesManager.php
* oldClassConstructors
 * Line 23: `	function GMModuleManager($p_module_type, $p_show_installed_modules_menu = false, $p_display_installed_modules = false, $p_show_missing_modules_menu = true, $p_display_missing_modules = true, $p_ignore_files_array = array())`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\GMOpenSearch.php
* oldClassConstructors
 * Line 81: `		function GMOpenSearch() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\GMOrderFormat.php
* oldClassConstructors
 * Line 21: `		function GMOrderFormat() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\GMProductExport.php
* oldClassConstructors
 * Line 54: `  function GMProductExport()`
* deprecatedFunctions
 * Line 875: `      $t_gm_get_shippingtime = mysql_query("SELECT shipping_status_name, number_of_days`
 * Line 879: `      if (mysql_num_rows($t_gm_get_shippingtime) == 1) {`
 * Line 880: `        $t_gm_shippingtime = mysql_fetch_array($t_gm_get_shippingtime);`
 * Line 945: `      $t_num_rows = mysql_num_rows($t_attributes_query);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\GMProductUpload.php
* oldClassConstructors
 * Line 21: `		function GMProductUpload($file, $new_file_name='', $prd_id, $more_image_prev='', $more_image_nr='', $first_image='', $more_image=false) {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\GMSitemapXML.php
* oldClassConstructors
 * Line 103: `		function GMSitemapXML($ping) `

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\GMStart.php
* oldClassConstructors
 * Line 33: `		function GMStart() {			`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\GMStat.php
* oldClassConstructors
 * Line 18: `		function GMStat() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\GMUpload.php
* oldClassConstructors
 * Line 25: `		function GMUpload($file, $file_rename, $file_dir, $file_oldname='') {		`
 * Line 137: `		function GMCatUpload($file, $file_rename, $file_dir, $file_oldname='', $sql_id='') {	`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\ShowLogs.php
* oldClassConstructors
 * Line 21: `    function ShowLogs()`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\gmOrderPDF.php
* oldClassConstructors
 * Line 103: `		function gmOrderPDF($type, $order_right, $order_data, $order_total, $order_info, $pdf_footer, $pdf_fonts, $gm_pdf_values, $gm_order_pdf_values, $gm_use_products_model) {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\gmPDF.php
* oldClassConstructors
 * Line 64: `		function gmPDF($gm_pdf_values) {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\phplot\phplot.php
* oldClassConstructors
 * Line 168: `    function PHPlot($which_width=600, $which_height=400, $which_output_file=NULL, $which_input_file=NULL)`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\phplot\phplot_data.php
* oldClassConstructors
 * Line 20: `    function PHPlot_Data($which_width=600, $which_height=400, $which_output_file=NULL, $which_input_file=NULL)`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\fckeditor\fckeditor_php4.php
* oldClassConstructors
 * Line 126: `	function FCKeditor( $instanceName )`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\affilinet.php
* oldClassConstructors
 * Line 31: `	function Affilinet() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\belboon.php
* oldClassConstructors
 * Line 31: `	function Belboon() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\billiger.php
* oldClassConstructors
 * Line 31: `	function Billiger() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\biologisch.php
* oldClassConstructors
 * Line 31: `	function Biologisch() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\carmio.php
* oldClassConstructors
 * Line 29: `	function Carmio() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\ciao.php
* oldClassConstructors
 * Line 31: `	function Ciao() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\commerceconnector.php
* oldClassConstructors
 * Line 31: `	function CommerceConnector() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\daparto.php
* oldClassConstructors
 * Line 31: `	function Daparto() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\dooyoo.php
* oldClassConstructors
 * Line 31: `	function Dooyoo() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\einfachbilliger.php
* oldClassConstructors
 * Line 31: `	function EinfachBilliger() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\evendi.php
* oldClassConstructors
 * Line 31: `	function Evendi() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\fashion.php
* oldClassConstructors
 * Line 31: `	function Fashion() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\froogle.php
* oldClassConstructors
 * Line 31: `	function Froogle() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\geizhals_at.php
* oldClassConstructors
 * Line 31: `	function Geizhals_AT() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\gimahhot.php
* oldClassConstructors
 * Line 31: `	function Gimahhot() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\google.php
* oldClassConstructors
 * Line 31: `	function Google() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\guenstiger.php
* oldClassConstructors
 * Line 31: `	function Guenstiger() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\idealo.php
* oldClassConstructors
 * Line 32: `  function Idealo() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\kauflux.php
* oldClassConstructors
 * Line 31: `	function Kauflux() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\kelkoo.php
* oldClassConstructors
 * Line 32: `	function Kelkoo() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\kelkoo_basis.php
* oldClassConstructors
 * Line 31: `	function Kelkoo_Basis() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\kelkoo_premium.php
* oldClassConstructors
 * Line 31: `	function Kelkoo_Premium() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\laary.php
* oldClassConstructors
 * Line 31: `	function Laary() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\ladenzeile.php
* oldClassConstructors
 * Line 31: `	function Ladenzeile() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\leguide.php
* oldClassConstructors
 * Line 31: `  function LeGuide() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\markencafe.php
* oldClassConstructors
 * Line 31: `	function Markencafe() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\metashopper.php
* oldClassConstructors
 * Line 31: `	function Metashopper() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\milando.php
* oldClassConstructors
 * Line 31: `	function Milando() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\moebel.php
* oldClassConstructors
 * Line 31: `	function Moebel() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\motoso.php
* oldClassConstructors
 * Line 32: `	function Motoso() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\mysport.php
* oldClassConstructors
 * Line 31: `	function MySport() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\nextag.php
* oldClassConstructors
 * Line 31: `	function Nextag() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\pangora.php
* oldClassConstructors
 * Line 31: `	function Pangora() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\piazza_ch.php
* oldClassConstructors
 * Line 31: `	function Piazza_ch() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\preis.php
* oldClassConstructors
 * Line 31: `	function Preis() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\preisbase.php
* oldClassConstructors
 * Line 31: `	function Preisbase() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\preisroboter.php
* oldClassConstructors
 * Line 31: `	function Preisroboter() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\preissuchmaschine.php
* oldClassConstructors
 * Line 31: `	function Preissuchmaschine() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\preisvergleich.php
* oldClassConstructors
 * Line 31: `	function Preisvergleich() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\promago.php
* oldClassConstructors
 * Line 32: `  function Promago() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\restposten.php
* oldClassConstructors
 * Line 31: `	function Restposten() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\shopping.php
* oldClassConstructors
 * Line 31: `	function Shopping() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\shopping24.php
* oldClassConstructors
 * Line 31: `	function Shopping24() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\shopzilla.php
* oldClassConstructors
 * Line 31: `	function Shopzilla() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\smatch.php
* oldClassConstructors
 * Line 31: `	function Smatch() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\stylight.php
* oldClassConstructors
 * Line 31: `	function Stylight() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\superclix.php
* oldClassConstructors
 * Line 31: `	function Superclix() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\webgains.php
* oldClassConstructors
 * Line 31: `	function Webgains() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\zanox.php
* oldClassConstructors
 * Line 31: `	function Zanox() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\gm_product_export\zentralverkauf.php
* oldClassConstructors
 * Line 31: `	function Zentralverkauf() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm_guestbook.php
* deprecatedFunctions
 * Line 25: `			mysql_query("TRUNCATE gm_guestbook_customers_status");`
 * Line 27: `				mysql_query("INSERT INTO gm_guestbook_customers_status`
 * Line 57: `	$gm_get_customers_status = mysql_query("SELECT`
 * Line 64: `	while($row = mysql_fetch_array($gm_get_customers_status)){`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm_sql.php
* deprecatedFunctions
 * Line 29: `			$gm_query_result = mysql_query($gm_query[$i]);`
 * Line 30: `			if(!$gm_query_result) $gm_query_result_output .= GM_SQL_ERROR . mysql_error() . '<br />';`
 * Line 105: `      $gm_query_result = mysql_query($gm_query[$i]); // xtc_db_query hier nicht verwenden!`
 * Line 106: `      if(!$gm_query_result) $gm_query_result_output .= GM_SQL_ERROR . mysql_error() . '<br />';`
 * Line 109: `      $num_fields = mysql_num_fields($gm_query_result);`
 * Line 112: `        $headers[] = mysql_field_name($gm_query_result , $i);`
 * Line 237: `						if(isset($gm_query_result_output)) echo "<p>".$gm_query_result_output." Es wurden ".mysql_num_rows($gm_query_result)." Ergebnisse gefunden.</p>";`
 * Line 244: `  								for($i = 0; $i < mysql_num_fields($gm_query_result); $i++){`
 * Line 245: `  									$name = mysql_field_name($gm_query_result, $i);`
 * Line 253: `  							for($i = 0; $i < mysql_num_rows($gm_query_result); $i++){`
 * Line 257: `  								for($h = 0; $h < mysql_num_fields($gm_query_result); $h++){`
 * Line 258: `  									$name = mysql_field_name($gm_query_result, $h);`
 * Line 260: `                      $value = mysql_result($gm_query_result, $i, $name);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm_trusted_info.php
* deprecatedFunctions
 * Line 29: `			$gm_query_result = mysql_query($gm_query[$i]); // xtc_db_query hier nicht verwenden!`
 * Line 30: `			if(!$gm_query_result) $gm_query_result_output .= GM_SQL_ERROR . mysql_error() . '<br />';`

#### C:\Users\marti\Documents\gambio_tickets75\admin\gm_trusted_shop_id.php
* deprecatedFunctions
 * Line 34: `			mysql_query('`
 * Line 40: `		mysql_query('UPDATE gm_configuration SET gm_value="'.$_POST['trusted_shop_id'] .'" WHERE gm_key="TRUSTED_SHOP_ID"');`
 * Line 41: `		echo mysql_error();`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\afterbuy_parse_beschreibung_neu.03.2016.php
* duplicateFunctionParameter
 * Line 1579: `function insert_attribute($products_id, $ab_prod_model, $ab_prod_id, $ab_product_sell_price, $ab_quantity, $basisproduktname, $produktname, $ab_variations_name, $product_weight, $save_attributname = "Kategorie", $ab_quantity, $language_id, $produktset, $variation_product)`
* deprecatedFunctions
 * Line 1738: `					WHERE language_id = '".mysql_real_escape_string($language_id['languages_id'])."' `
 * Line 1744: `						VALUES 	 ('".$option_id."' , '".$language_id['languages_id']."' , '".mysql_real_escape_string($options_values_name)."') ";`
 * Line 1754: `					WHERE products_options_values_name = '".mysql_real_escape_string($options_values_name)."'";`
 * Line 1835: `						VALUES 	 ('".$option_id."' , '".$language_id['languages_id']."' , '".mysql_real_escape_string($options_name)."') ";`
 * Line 1846: `					WHERE products_options_name= '".mysql_real_escape_string($options_name)."'";`
 * Line 2900: `	$link = mysql_connect(DB_SERVER, DB_SERVER_USERNAME, DB_SERVER_PASSWORD, DB_DATABASE);`
 * Line 2901: `	$charset = mysql_client_encoding($link);`
 * Line 2903: `	mysql_close($link);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\afterbuy_parse_beschreibung_neu.06.2015.php
* duplicateFunctionParameter
 * Line 1576: `function insert_attribute($products_id, $ab_prod_model, $ab_prod_id, $ab_product_sell_price, $ab_quantity, $basisproduktname, $produktname, $ab_variations_name, $product_weight, $save_attributname = "Kategorie", $ab_quantity, $language_id, $produktset, $variation_product)`
* deprecatedFunctions
 * Line 1735: `					WHERE language_id = '".mysql_real_escape_string($language_id['languages_id'])."' `
 * Line 1741: `						VALUES 	 ('".$option_id."' , '".$language_id['languages_id']."' , '".mysql_real_escape_string($options_values_name)."') ";`
 * Line 1751: `					WHERE products_options_values_name = '".mysql_real_escape_string($options_values_name)."'";`
 * Line 1832: `						VALUES 	 ('".$option_id."' , '".$language_id['languages_id']."' , '".mysql_real_escape_string($options_name)."') ";`
 * Line 1843: `					WHERE products_options_name= '".mysql_real_escape_string($options_name)."'";`
 * Line 2897: `	$link = mysql_connect(DB_SERVER, DB_SERVER_USERNAME, DB_SERVER_PASSWORD, DB_DATABASE);`
 * Line 2898: `	$charset = mysql_client_encoding($link);`
 * Line 2900: `	mysql_close($link);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\application_top.php
* deprecatedFunctions
 * Line 342: `mysql_query("SET NAMES 'utf8'");`
 * Line 343: `mysql_query("SET CHARACTER SET utf8");`
 * Line 344: `mysql_query("SET SESSION collation_connection = 'utf8_unicode_ci'");`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\classes\campaigns.php
* oldClassConstructors
 * Line 14: `	function campaigns(& $get_array) {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\classes\categories.php
* deprecatedFunctions
 * Line 1421: `												gm_alt_text	= '" . mysql_real_escape_string($row['gm_alt_text'])								. "'`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\classes\image_manipulator_GD1.php
* oldClassConstructors
 * Line 17: `	function image_manipulation($resource_file, $max_width, $max_height, $destination_file="", $compression=80, $transform="")`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\classes\image_manipulator_GD2.php
* oldClassConstructors
 * Line 17: `	function image_manipulation($resource_file, $max_width, $max_height, $destination_file="", $compression=IMAGE_QUALITY, $transform="")`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\classes\import.php
* oldClassConstructors
 * Line 16: `	function xtcImport($filename) {`
 * Line 614: `	function xtcExport($filename) {`
* deprecatedFunctions
 * Line 279: `			$this->mfn[$manufacturer]['id'] = mysql_insert_id();`
 * Line 368: `			if(!isset($products_id)) $products_id = mysql_insert_id();`
 * Line 511: `						$cat_id = mysql_insert_id();`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\classes\order.php
* oldClassConstructors
 * Line 31: `    function order($order_id)`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\classes\pclzip.lib.php
* deprecatedFunctions
 * Line 5080: `	$this->magic_quotes_status = @get_magic_quotes_runtime();`
 * Line 5085: `	  @set_magic_quotes_runtime(0);`
 * Line 5118: `  	  @set_magic_quotes_runtime($this->magic_quotes_status);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\classes\session\MysqlSessionHandler.php
* deprecatedFunctions
 * Line 54: `        if(!@mysql_ping()) {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\functions\database.php
* variableInterpolation
 * Line 16: `    global $$link;`
 * Line 27: `    global $$link_service;`
 * Line 37: `    global $$link;`
 * Line 42: `    global $$link_service;`
 * Line 49: `    global $$link, $logger;`
 * Line 62: `    global $$link_service, $logger_service;`
* deprecatedFunctions
 * Line 18: `      $$link = mysql_pconnect($server, $username, $password);`
 * Line 20: `      $$link = mysql_connect($server, $username, $password);`
 * Line 22: `    if ($$link) mysql_select_db($database);`
 * Line 29: `      $$link_service = mysql_pconnect($server_service, $username_service, $password_service);`
 * Line 31: `      $$link_service = mysql_connect($server_service, $username_service, $password_service);`
 * Line 33: `    if ($$link_service) mysql_select_db($database_service);`
 * Line 38: `    return mysql_close($$link);`
 * Line 43: `    return mysql_close($$link_service);`
 * Line 54: `    $result = mysql_query($query, $$link) or xtc_db_error($query, mysql_errno(), mysql_error());`
 * Line 56: `      if (mysql_error()) $logger->write(mysql_error(), 'ERROR');`
 * Line 67: `    $result = mysql_query($query, $$link_service) or xtc_db_error($query, mysql_errno(), mysql_error());`
 * Line 69: `      if (mysql_error()) $logger_service->write(mysql_error(), 'ERROR');`
 * Line 117: `    return mysql_fetch_array($db_query, MYSQL_ASSOC);`
 * Line 120: `    return mysql_result($result, $row, $field);`
 * Line 123: `    return mysql_num_rows($db_query);`
 * Line 126: `    return mysql_data_seek($db_query, $row_number);`
 * Line 129: `    return mysql_insert_id();`
 * Line 132: `    return mysql_free_result($db_query);`
 * Line 136: `    return mysql_fetch_row($db_query);`
 * Line 139: `    return mysql_fetch_field($db_query);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\functions\general.php
* deprecatedFunctions
 * Line 802: `	return array ('date' => xtc_datetime_short(date('Y-m-d H:i:s')), 'system' => $system, 'kernel' => $kernel, 'host' => $host, 'ip' => gethostbyname($host), 'uptime' => @ exec('uptime'), 'http_server' => $_SERVER['SERVER_SOFTWARE'], 'php' => PHP_VERSION, 'zend' => (function_exists('zend_version') ? zend_version() : ''), 'db_server' => DB_SERVER, 'db_ip' => gethostbyname(DB_SERVER), 'db_version' => 'MySQL '. (function_exists('mysql_get_server_info') ? mysql_get_server_info() : ''), 'db_date' => xtc_datetime_short($db['datetime']));`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\brickfox\export.php
* oldClassConstructors
 * Line 27: `	function export()`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\brickfox\import.php
* oldClassConstructors
 * Line 22: `	function import()`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\brickfox\lib\BrickfoxConfiguration.php
* oldClassConstructors
 * Line 29: `	function Brickfox_Lib_BrickfoxConfiguration($url = '', $port = '', $username = '', $password = '', $excludeCategories = '', $excludeProducts = '', $status = false)`
* deprecatedFunctions
 * Line 48: `		$valueList = mysql_real_escape_string(trim($valueString, ','));`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\brickfox\lib\Export.php
* oldClassConstructors
 * Line 32: `	function Brickfox_Lib_Export(Brickfox_Lib_BrickfoxConfiguration $brickfoxConfiguration, $type, $lastExport = null)`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\brickfox\lib\Import.php
* deprecatedFunctions
 * Line 92: `		return mysql_real_escape_string(utf8_decode($data));`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\brickfox\lib\_rest\RestClient.php
* oldClassConstructors
 * Line 25: `	function brickfox_RestClient(Brickfox_Lib_BrickfoxConfiguration $brickfoxConfiguration)`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\export\billiger.php
* oldClassConstructors
 * Line 41: `	function billiger() {`
* deprecatedFunctions
 * Line 133: `			$gm_get_shippingtime = mysql_query("SELECT`
 * Line 139: `			if(mysql_num_rows($gm_get_shippingtime) == 1){`
 * Line 140: `				$gm_shippingtime = mysql_fetch_array($gm_get_shippingtime);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\export\ciao.php
* deprecatedFunctions
 * Line 152: `	$mb_get_shippingtime = mysql_query("SELECT`
 * Line 158: `		if(mysql_num_rows($mb_get_shippingtime) == 1){`
 * Line 159: `			$mb_shippingtime = mysql_fetch_array($mb_get_shippingtime);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\export\dooyoo.php
* oldClassConstructors
 * Line 40: `	function dooyoo() {`
* deprecatedFunctions
 * Line 137: `			$mb_get_shippingtime = mysql_query("SELECT`
 * Line 143: `			if(mysql_num_rows($mb_get_shippingtime) == 1){`
 * Line 144: `				$mb_shippingtime = mysql_fetch_array($mb_get_shippingtime);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\export\froogle.php
* oldClassConstructors
 * Line 42: `	function froogle() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\export\gambio_error_report.php
* oldClassConstructors
 * Line 60: `	function gambio_error_report() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\export\gambio_janolaw.php
* oldClassConstructors
 * Line 32: `	function gambio_janolaw() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\export\geizhals.php
* oldClassConstructors
 * Line 41: `	function geizhals() {`
* deprecatedFunctions
 * Line 132: `				$gm_shippingtime = mysql_fetch_array($gm_get_shippingtime);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\export\geizkragen.php
* deprecatedFunctions
 * Line 153: `	$mb_get_shippingtime = mysql_query("SELECT`
 * Line 159: `	if(mysql_num_rows($mb_get_shippingtime) == 1){`
 * Line 160: `		$mb_shippingtime = mysql_fetch_array($mb_get_shippingtime);`
 * Line 162: `	$mb_get_categorie_name = mysql_query("SELECT`
 * Line 173: `	if(mysql_num_rows($mb_get_categorie_name) == 1){`
 * Line 174: `		$mb_categories_name = mysql_fetch_array($mb_get_categorie_name);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\export\idealo.php
* oldClassConstructors
 * Line 42: `	function idealo() {`
* deprecatedFunctions
 * Line 136: `			$gm_get_shippingtime = mysql_query("SELECT`
 * Line 142: `			if(mysql_num_rows($gm_get_shippingtime) == 1){`
 * Line 143: `				$gm_shippingtime = mysql_fetch_array($gm_get_shippingtime);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\export\image_processing.php
* oldClassConstructors
 * Line 26: `	function image_processing() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\export\milando.php
* oldClassConstructors
 * Line 40: `	function milando() {`
* deprecatedFunctions
 * Line 134: `			$mb_get_shippingtime = mysql_query("SELECT`
 * Line 140: `			if(mysql_num_rows($mb_get_shippingtime) == 1){`
 * Line 141: `				$mb_shippingtime = mysql_fetch_array($mb_get_shippingtime);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\export\pangora.php
* oldClassConstructors
 * Line 40: `	function pangora() {`
* deprecatedFunctions
 * Line 136: `			$mb_get_shippingtime = mysql_query("SELECT`
 * Line 142: `			if(mysql_num_rows($mb_get_shippingtime) == 1){`
 * Line 143: `				$mb_shippingtime = mysql_fetch_array($mb_get_shippingtime);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\export\preisauskunft.php
* oldClassConstructors
 * Line 41: `	function preisauskunft() {`
* deprecatedFunctions
 * Line 133: `			$gm_get_shippingtime = mysql_query("SELECT`
 * Line 139: `			if(mysql_num_rows($gm_get_shippingtime) == 1){`
 * Line 140: `				$gm_shippingtime = mysql_fetch_array($gm_get_shippingtime);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\export\preisfuchs.php
* oldClassConstructors
 * Line 41: `	function preisfuchs() {`
* deprecatedFunctions
 * Line 133: `			$gm_get_shippingtime = mysql_query("SELECT`
 * Line 139: `			if(mysql_num_rows($gm_get_shippingtime) == 1){`
 * Line 140: `				$gm_shippingtime = mysql_fetch_array($gm_get_shippingtime);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\export\preisomat.php
* oldClassConstructors
 * Line 41: `	function preisomat() {`
* deprecatedFunctions
 * Line 126: `			$mb_get_shippingtime = mysql_query("SELECT`
 * Line 132: `			if(mysql_num_rows($mb_get_shippingtime) == 1){`
 * Line 133: `				$mb_shippingtime = mysql_fetch_array($mb_get_shippingtime);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\export\preisroboter.php
* oldClassConstructors
 * Line 41: `	function preisroboter() {`
* deprecatedFunctions
 * Line 136: `			$mb_get_shippingtime = mysql_query("SELECT`
 * Line 142: `			if(mysql_num_rows($mb_get_shippingtime) == 1){`
 * Line 143: `				$mb_shippingtime = mysql_fetch_array($mb_get_shippingtime);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\export\shopping.php
* oldClassConstructors
 * Line 40: `	function shopping() {`
* deprecatedFunctions
 * Line 135: `			$mb_get_shippingtime = mysql_query("SELECT`
 * Line 141: `			if(mysql_num_rows($mb_get_shippingtime) == 1){`
 * Line 142: `				$mb_shippingtime = mysql_fetch_array($mb_get_shippingtime);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\export\xtbooster.php
* oldClassConstructors
 * Line 36: `    function xtbooster() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\gm_export\delisprint.php
* oldClassConstructors
 * Line 42: `	function delisprint() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\gm_export\gls.php
* oldClassConstructors
 * Line 42: `	function gls() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\gm_export\hermes.php
* oldClassConstructors
 * Line 42: `	function hermes() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\new_attributes_change.php
* deprecatedFunctions
 * Line 117: `//    xtc_db_query("INSERT INTO ".TABLE_PRODUCTS_ATTRIBUTES." (products_id, options_id, options_values_id, options_values_price, price_prefix ,attributes_model, attributes_stock, options_values_weight, weight_prefix, sortorder, products_vpe_id, gm_vpe_value, gm_ean) VALUES ('" . $_POST['current_product_id'] . "', '" . $optionsID . "', '" . $_POST['optionValues'][$i] . "', '" . $value_price . "', '" . $value_prefix . "', '" . $value_model . "', '" . $value_stock . "', '" . $value_weight . "', '" . $value_weight_prefix . "', '".$value_sortorder."', '".$gm_vpe_id."', '".$gm_vpe_value."', '".$gm_ean."')") or die(mysql_error());`
 * Line 119: `    xtc_db_query("INSERT INTO ".TABLE_PRODUCTS_ATTRIBUTES." (products_id, options_id, options_values_id, options_values_price, price_prefix ,attributes_model, attributes_stock, options_values_weight, weight_prefix, sortorder, products_vpe_id, gm_vpe_value, gm_ean, allowed_shipping_modules, allowed_payment_modules, gift_wrap, gift_price, voucher, voucher_price, qty_even, qty_odd, max_qty) VALUES ('" . $_POST['current_product_id'] . "', '" . $optionsID . "', '" . $_POST['optionValues'][$i] . "', '" . $value_price . "', '" . $value_prefix . "', '" . $value_model . "', '" . $value_stock . "', '" . $value_weight . "', '" . $value_weight_prefix . "', '".$value_sortorder."', '".$gm_vpe_id."', '".$gm_vpe_value."', '".$gm_ean."', '".$value_allowed_ship_mod."', '".$value_allowed_pay_mod."', '".$gift_wrap."', '".$gift_price."', '".$voucher."', '".$voucher_price."', '".$qty_even."', '".$qty_odd."', '".$max_qty."')") or die(mysql_error());`
 * Line 127: `        xtc_db_query("INSERT INTO ".TABLE_PRODUCTS_ATTRIBUTES_DOWNLOAD." (products_attributes_id, products_attributes_filename, products_attributes_maxdays, products_attributes_maxcount) VALUES ('" . $products_attributes_id . "', '" . $value_download_file . "', '" . $value_download_expire . "', '" . $value_download_count . "')") or die(mysql_error());`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\new_attributes_functions.php
* deprecatedFunctions
 * Line 34: `        $dl_sql = xtc_db_query("SELECT products_attributes_maxdays, products_attributes_filename, products_attributes_maxcount FROM ".TABLE_PRODUCTS_ATTRIBUTES_DOWNLOAD." WHERE products_attributes_id = '" . $line['products_attributes_id'] . "'") or die(mysql_error());`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\tickets75\eventmap\helper\event_map_edit_legend_values_iframe.php
* deprecatedFunctions
 * Line 82: `	mysql_query("set names ".$_SESSION['language_charset']);`
 * Line 83: `	mysql_query('SET CHARACTER SET '.$_SESSION['language_charset']) ;`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\yatego\CYYatArtSel.php
* oldClassConstructors
 * Line 13: `	function CYYatArtSel() {`
* deprecatedFunctions
 * Line 128: `			while ($row = mysql_fetch_row($result)) {`
 * Line 182: `				while ($row = mysql_fetch_assoc($result)) `
 * Line 200: `				while($row = mysql_fetch_assoc($result)) `
 * Line 224: `				while ($row = mysql_fetch_assoc($result)) `
 * Line 243: `			$total_pages = mysql_fetch_row($result);`
 * Line 276: `			while ($row = mysql_fetch_row($result)) {`
 * Line 310: `		while($row = mysql_fetch_row($result)) {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\yatego\CYYatMap.php
* oldClassConstructors
 * Line 8: `	function CYYatMap() {`
* deprecatedFunctions
 * Line 24: `		mysql_query("SET OPTION SQL_Max_JOIN=500000000000"); `
 * Line 62: `		while ($row = mysql_fetch_row($result)) {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\modules\yatego\CYYatPref.php
* oldClassConstructors
 * Line 18: `	function CYYatPref() {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\xmlparserv4.php
* oldClassConstructors
 * Line 19: `    function XMLParser($xml){`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\xsbooster\xsb_functions.php
* variableInterpolation
 * Line 95: `    global $$link, $logger;`
* deprecatedFunctions
 * Line 101: `    $result = mysql_query($query, $$link);`
 * Line 102: `    } while (2006 == mysql_errno());`
 * Line 103: `    if(0 != mysql_errno()) { xtc_db_error($query, mysql_errno(), mysql_error()); }`
 * Line 105: `      if (mysql_error()) $logger->write(mysql_error(), 'ERROR');`

#### C:\Users\marti\Documents\gambio_tickets75\admin\interkurierConnect.php
* deprecatedFunctions
 * Line 11: `$iName = mysql_fetch_object($interkurier);`
 * Line 44: `		$o = mysql_fetch_object($order_query);`
 * Line 49: `		while($op = mysql_fetch_object($order_products)){`
 * Line 51: `			$weight = mysql_fetch_object($weight_query);`
 * Line 55: `		$ot = mysql_fetch_object($order_total);`

#### C:\Users\marti\Documents\gambio_tickets75\admin\orders.php
* deprecatedFunctions
 * Line 1297: `            if ($qr_ems && mysql_num_rows($qr_ems) > 0) {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\products_attributes.php
* deprecatedFunctions
 * Line 536: `while($row = mysql_fetch_array($mod_search_productid_query)){`
 * Line 542: `    while($rowloc = mysql_fetch_array($mod_search_location_query)){`
 * Line 556: `while($row2 = mysql_fetch_array($mod_search_productid_query2)){ `
 * Line 562: `while($row3 = mysql_fetch_array($mod_search_attributes_query)){ `
 * Line 568: `    while($row4 = mysql_fetch_array($mod_search_attributename_query)){ `

#### C:\Users\marti\Documents\gambio_tickets75\admin\products_attributes_old.php
* deprecatedFunctions
 * Line 1104: `while($row = mysql_fetch_array($mod_search_productid_query)){`
 * Line 1112: `    while($row2 = mysql_fetch_array($mod_search_productid_query2)){`
 * Line 1145: `    while($row2 = mysql_fetch_array($mod_search_productid_query2)){`
 * Line 1149: `    while($row3 = mysql_fetch_array($mod_search_productid_query3)){`
 * Line 1162: `/* while($row = mysql_fetch_array($mod_search_productid_query)){`

#### C:\Users\marti\Documents\gambio_tickets75\admin\products_attributes_working.php
* deprecatedFunctions
 * Line 531: `while($row = mysql_fetch_array($mod_search_productid_query)){`

#### C:\Users\marti\Documents\gambio_tickets75\admin\request_port.php
* deprecatedFunctions
 * Line 72: `mysql_close();`

#### C:\Users\marti\Documents\gambio_tickets75\admin\template_configuration.php
* oldClassConstructors
 * Line 20: `	function TemplateConfiguration()`
* deprecatedFunctions
 * Line 45: `		$c_attr = mysql_real_escape_string($p_attr);`
 * Line 46: `		$c_value = mysql_real_escape_string($p_value);`
 * Line 60: `						s.template_name = '" . mysql_real_escape_string(CURRENT_TEMPLATE) . "' AND`
 * Line 76: `		$c_attr = mysql_real_escape_string($p_attr);`
 * Line 86: `							s.template_name = '" . mysql_real_escape_string(CURRENT_TEMPLATE) . "' AND`
 * Line 100: `							s.template_name = '" . mysql_real_escape_string(CURRENT_TEMPLATE) . "' AND`
 * Line 127: `		$c_attr = mysql_real_escape_string(trim($p_attr));`
 * Line 128: `		$c_old_value = mysql_real_escape_string(trim($p_old_value));`
 * Line 129: `		$c_new_value = mysql_real_escape_string(trim($p_new_value));`
 * Line 222: `							s.template_name = '" . mysql_real_escape_string(CURRENT_TEMPLATE) . "' AND`
 * Line 223: `							s.style_name = '" . mysql_real_escape_string($t_css_selectors_array[$i]) . "' AND`
 * Line 236: `								s.template_name = '" . mysql_real_escape_string(CURRENT_TEMPLATE) . "' AND`
 * Line 237: `								s.style_name = '" . mysql_real_escape_string($t_css_selectors_array[$i]) . "' AND`
 * Line 251: `									s.template_name = '" . mysql_real_escape_string(CURRENT_TEMPLATE) . "' AND`
 * Line 252: `									s.style_name = '" . mysql_real_escape_string($t_css_selectors_array[$i]) . "' AND`
 * Line 260: `									SET style_value = '" . mysql_real_escape_string($t_margin_left) . "'`
 * Line 265: `									SET style_value = '" . mysql_real_escape_string($t_margin_right) . "'`
 * Line 275: `									SET style_value = '0 " . mysql_real_escape_string($t_margin_right) . " 0 " .  mysql_real_escape_string($t_margin_left) . " 0'`

#### C:\Users\marti\Documents\gambio_tickets75\admin\xtbooster.php
* deprecatedFunctions
 * Line 95: `	$data		= mysql_fetch_assoc($rlResult);`
 * Line 173: `						WHERE XTB_ITEM_ID='". mysql_result(xsb_db_query("SELECT LAST_INSERT_ID() as last_insert_id FROM xtb_auctions"),0,'last_insert_id') ."'");`
 * Line 2449: `				$year_start = date('Y', mysql_result(xsb_db_query("SELECT MIN(_EBAY_START_TIME) as MinTime FROM xtb_auctions"),0,'MinTime'));`
 * Line 2468: `				$year_start = date('Y', mysql_result(xsb_db_query("SELECT MIN(_EBAY_START_TIME) as MinTime FROM xtb_auctions"),0,'MinTime'));`

#### C:\Users\marti\Documents\gambio_tickets75\admin\yatego.php
* deprecatedFunctions
 * Line 78: `													$row = mysql_fetch_row($result);`
 * Line 83: `													while ($row = mysql_fetch_row($result)) {`
 * Line 116: `													while ($row2 = mysql_fetch_row($result2)) `

#### C:\Users\marti\Documents\gambio_tickets75\admin\yoochoose\usage_data_tools.php
* deprecatedFunctions
 * Line 384: `        $query = sprintf("show table status like '%s'", mysql_real_escape_string($tableName));`

#### C:\Users\marti\Documents\gambio_tickets75\admin\yoochoose\utils.php
* deprecatedFunctions
 * Line 23: `        xtc_db_query(sprintf($sql, mysql_real_escape_string($name), mysql_real_escape_string($value)));`
 * Line 54: `                mysql_real_escape_string(CURRENT_TEMPLATE), `
 * Line 55: `                mysql_real_escape_string($boxName)));`
 * Line 65: `                mysql_real_escape_string($enabled ? 1 : 0), `
 * Line 66: `                mysql_real_escape_string(CURRENT_TEMPLATE),`
 * Line 67: `                mysql_real_escape_string($boxName),`
 * Line 68: `                mysql_real_escape_string($position)));`
 * Line 103: `                        WHERE c.gm_key = '" . mysql_real_escape_string($name) . "' ORDER BY l.sort_order";`

#### C:\Users\marti\Documents\gambio_tickets75\automatik_import\afterbuy_cron_functions.php
* deprecatedFunctions
 * Line 43: `    $dateTime = mysql_escape_string($dateTime);`
 * Line 54: `    $request = mysql_real_escape_string($request);`
 * Line 55: `    $response = mysql_real_escape_string($response);`

#### C:\Users\marti\Documents\gambio_tickets75\automatik_import\image_manipulator_GD2.php
* oldClassConstructors
 * Line 16: `	function image_manipulation($resource_file, $max_width, $max_height, $destination_file="", $compression=IMAGE_QUALITY, $transform="")`

#### C:\Users\marti\Documents\gambio_tickets75\automatik_import\product_refresh\DatabaseClient.php
* deprecatedFunctions
 * Line 18: `        $parameter = @mysql_escape_string($keyPattern . '%');`
 * Line 67: `                    @mysql_escape_string((string) utf8_decode($item['name'])),`

#### C:\Users\marti\Documents\gambio_tickets75\callback\moneybookers\moneybookers.php
* oldClassConstructors
 * Line 14: ` 		function moneybookers_callback() {`

#### C:\Users\marti\Documents\gambio_tickets75\callback\sofort\callback.php
* deprecatedFunctions
 * Line 209: `	if (function_exists('mysql_affected_rows') && mysql_affected_rows() == '1') HelperFunctions::insertHistoryEntry($orderId, HelperFunctions::getLastOrderStatus($orderId), MODULE_PAYMENT_SOFORT_MULTIPAY_TRANSACTION_ID.': '.$tId);`

#### C:\Users\marti\Documents\gambio_tickets75\callback\sofort\helperFunctions.php
* deprecatedFunctions
 * Line 152: `		return (function_exists('mysql_real_escape_string') && mysql_ping()) ? mysql_real_escape_string($string) : mysql_escape_string($string);`
 * Line 602: `				switch (mysql_affected_rows()) {`
 * Line 630: `				switch (mysql_affected_rows()) {`
 * Line 738: `		$result = mysql_query('SELECT orders_ident_key FROM '.HelperFunctions::escapeSql(TABLE_ORDERS).' WHERE orders_id = "'.HelperFunctions::escapeSql($orderId).'"');`

#### C:\Users\marti\Documents\gambio_tickets75\callback\sofort\library\helper\pnag_customer.php
* oldClassConstructors
 * Line 69: `	public function PnagCustomer($name = '', $lastname = '', $firstname = '', $company = '', $csID = '', $vatId = '', $shopId = '', $Id = '', $cIP = '', $streetAddress = '', $suburb = '', $city = '', $postcode = '', $state = '', $country = '', $formatId = '', $telephone = '', $emailAddress = '') {`

#### C:\Users\marti\Documents\gambio_tickets75\callback\sofort\library\sofortLib_Logger.inc.php
* oldClassConstructors
 * Line 27: `	public function SofortLibLogger() {`

#### C:\Users\marti\Documents\gambio_tickets75\callback\sofort\sofort.php
* deprecatedFunctions
 * Line 998: `						$result = mysql_query('`
 * Line 1004: `						while(($row = mysql_fetch_array($result) )) {`
 * Line 1006: `							mysql_query('`
 * Line 1010: `							//echo mysql_error(); //buyer ist not allowed to see this`

#### C:\Users\marti\Documents\gambio_tickets75\checkout_confirmation.php
* variableInterpolation
 * Line 106: `if ((is_array($payment_modules->modules) && (sizeof($payment_modules->selection()) > 1) && (!is_object($$_SESSION['payment'])) && (!isset ($_SESSION['credit_covers']))) || (is_object($$_SESSION['payment']) && ($$_SESSION['payment']->enabled == false))) {`
 * Line 402: `if (isset ($$_SESSION['payment']->form_action_url) && !$$_SESSION['payment']->tmpOrders) {`
 * Line 403: `	$form_action_url = $$_SESSION['payment']->form_action_url;`
 * Line 410: `if(method_exists($$_SESSION['payment'], 'confirm_pre_form'))`
 * Line 412: `	$sPreForm = $$_SESSION['payment']->confirm_pre_form();`

#### C:\Users\marti\Documents\gambio_tickets75\checkout_confirmation_ajax.php
* variableInterpolation
 * Line 106: `if ((is_array($payment_modules->modules) && (sizeof($payment_modules->selection()) > 1) && (!is_object($$_SESSION['payment'])) && (!isset ($_SESSION['credit_covers']))) || (is_object($$_SESSION['payment']) && ($$_SESSION['payment']->enabled == false))) {`
 * Line 402: `if (isset ($$_SESSION['payment']->form_action_url) && !$$_SESSION['payment']->tmpOrders) {`
 * Line 403: `	$form_action_url = $$_SESSION['payment']->form_action_url;`
 * Line 410: `if(method_exists($$_SESSION['payment'], 'confirm_pre_form'))`
 * Line 412: `	$sPreForm = $$_SESSION['payment']->confirm_pre_form();`

#### C:\Users\marti\Documents\gambio_tickets75\checkout_iclear.php
* variableInterpolation
 * Line 132: `if ((is_array($payment_modules->modules) && (sizeof($payment_modules->modules) > 1) && (!is_object($$_SESSION['payment'])) && (!isset ($_SESSION['credit_covers']))) || (is_object($$_SESSION['payment']) && ($$_SESSION['payment']->enabled == false))) {`
 * Line 160: `if (isset ($$_SESSION['payment']->form_action_url) && !$$_SESSION['payment']->tmpOrders) {`
 * Line 161: `	$form_action_url = $$_SESSION['payment']->form_action_url;`

#### C:\Users\marti\Documents\gambio_tickets75\checkout_onepage_process.php
* deprecatedFunctions
 * Line 72: `					if(mysql_num_rows($gm_attribute_stock) == 1) $gm_stock_error = true;`
 * Line 370: `					$gm_stock_data = mysql_fetch_array($gm_get_products_name);`
* variableInterpolation
 * Line 142: `	//if (isset ($$_SESSION['payment']->form_action_url) && $$_SESSION['payment']->tmpOrders) {`
 * Line 143: `	if ($$_SESSION['payment']->tmpOrders == true) {`
 * Line 145: `		$tmp_status = $$_SESSION['payment']->tmpStatus;`

#### C:\Users\marti\Documents\gambio_tickets75\checkout_process.php
* deprecatedFunctions
 * Line 63: `					if(mysql_num_rows($gm_attribute_stock) == 1) $gm_stock_error = true;`
 * Line 349: `				$gm_stock_data = mysql_fetch_array($gm_get_products_name);`
* variableInterpolation
 * Line 134: `	//if (isset ($$_SESSION['payment']->form_action_url) && $$_SESSION['payment']->tmpOrders) {`
 * Line 135: `	if ($$_SESSION['payment']->tmpOrders == true) {`
 * Line 137: `		$tmp_status = $$_SESSION['payment']->tmpStatus;`

#### C:\Users\marti\Documents\gambio_tickets75\checkout_success.1.php
* deprecatedFunctions
 * Line 190: `	$trusted_amount = round(mysql_result($trusted_result, 0, 'value'), 2);`
 * Line 191: `	//$trusted_amount = mysql_result($trusted_result, 0, 'value');`

#### C:\Users\marti\Documents\gambio_tickets75\checkout_success_old.php
* deprecatedFunctions
 * Line 121: `	$trusted_amount = round(mysql_result($trusted_result, 0, 'value'), 2);`
 * Line 122: `	//$trusted_amount = mysql_result($trusted_result, 0, 'value');`

#### C:\Users\marti\Documents\gambio_tickets75\export\cao_import.php
* oldClassConstructors
 * Line 63: `    function upload($file = '', $destination = '', $permissions = '777', $extensions = '') {`
* deprecatedFunctions
 * Line 390: `	          $products_id = mysql_insert_id();`
 * Line 604: `          $products_id = mysql_insert_id();`

#### C:\Users\marti\Documents\gambio_tickets75\ext\clickandbuy\lib\nusoap.php
* oldClassConstructors
 * Line 169: `	function nusoap_base() {`
 * Line 876: `	function soap_fault($faultcode,$faultactor='',$faultstring='',$faultdetail=''){`
 * Line 960: `	function XMLSchema($schema='',$xml='',$namespaces=array()){`
 * Line 1850: `  	function soapval($name='soapval',$type=false,$value=-1,$element_ns=false,$type_ns=false,$attributes=false) {`
 * Line 1921: `	function soap_transport_http($url){`
 * Line 3030: `	function soap_server($wsdl=false){`
 * Line 3922: `    function wsdl($wsdl = '',$proxyhost=false,$proxyport=false,$proxyusername=false,$proxypassword=false,$timeout=0,$response_timeout=30){`
 * Line 5613: `	function soap_parser($xml,$encoding='UTF-8',$method='',$decode_utf8=true){`
 * Line 6221: `	function nusoapclient($endpoint,$wsdl = false,$proxyhost = false,$proxyport = false,$proxyusername = false, $proxypassword = false, $timeout = 0, $response_timeout = 30){`
* deprecatedFunctions
 * Line 2255: `			set_magic_quotes_runtime(0);`
* newOperatorWithReference
 * Line 6242: `				$this->wsdl =& new wsdl($this->wsdlFile,$this->proxyhost,$this->proxyport,$this->proxyusername,$this->proxypassword,$this->timeout,$this->response_timeout);`

#### C:\Users\marti\Documents\gambio_tickets75\ext\clickandbuy\lib\xml_parser.php
* oldClassConstructors
 * Line 63: `    function XMLParser($xml = '', $cleanTagNames = true)`
 * Line 253: `    function XMLTag($name, $attrs = array(), $parents = 0)`

#### C:\Users\marti\Documents\gambio_tickets75\ext\clickandbuy\second_confirmation.php
* deprecatedFunctions
 * Line 28: `  if (!$qr || mysql_num_rows($qr) < 1) {`

#### C:\Users\marti\Documents\gambio_tickets75\gm\ajax\live_search.php
* deprecatedFunctions
 * Line 22: `$needle 				= mysql_real_escape_string($needle);`

#### C:\Users\marti\Documents\gambio_tickets75\gm\ajax\products_list.php
* deprecatedFunctions
 * Line 6: `$products_name 				= mysql_real_escape_string($products_name);`
 * Line 9: `$currrent_product_id 				= mysql_real_escape_string($currrent_product_id);`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\ErrorHandler.php
* oldClassConstructors
 * Line 14: `	function ErrorHandler()`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\FileLog.php
* oldClassConstructors
 * Line 16: `	function FileLog($p_file_base, $p_log_active=true)`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMAltText.php
* oldClassConstructors
 * Line 12: `		function GMAltText() {`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMAttributesCalculator.php
* oldClassConstructors
 * Line 20: `		function GMAttributesCalculator($products_id, $attributes, $tax_class_id, $p_combi_price = 0) {`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMCSSMonitor.php
* oldClassConstructors
 * Line 30: `		function GmImportCSS($css_code, $p_current_template) `
 * Line 218: `		function GMCSSMonitor($p_current_template) `
* deprecatedFunctions
 * Line 123: `					mysql_query('`
 * Line 128: `					$gm_css_style_id = mysql_insert_id();`
 * Line 137: `						mysql_query('`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMCSSOptimizer.php
* oldClassConstructors
 * Line 80: `		function GMCSSOptimizer($p_debug_mode, $p_style_edit)`
* deprecatedFunctions
 * Line 113: `			$t_result = mysql_query("`
 * Line 124: `			while($t_row = mysql_fetch_array($t_result))`
 * Line 127: `				$t_result_content = mysql_query('`
 * Line 138: `				while(($t_row_content = mysql_fetch_array($t_result_content) ))`
 * Line 358: `				$t_get_underline_setting = mysql_query("SELECT gm_value`
 * Line 363: `				if(mysql_num_rows($t_get_underline_setting) > 0)`
 * Line 434: `			$t_result = mysql_query("`
 * Line 445: `			while($t_row = mysql_fetch_array($t_result))`
 * Line 450: `					$t_result_content = mysql_query('`
 * Line 461: `					while($t_row_content = mysql_fetch_array($t_result_content))`
 * Line 692: `				$t_get_underline_setting = mysql_query("SELECT gm_value`
 * Line 697: `				if(mysql_num_rows($t_get_underline_setting) > 0)`
 * Line 771: `			$t_result = mysql_query("`
 * Line 781: `			if(mysql_num_rows($t_result) > 0)`
 * Line 783: `				while($t_row = mysql_fetch_array($t_result))`
 * Line 806: `				$t_result = mysql_query(`
 * Line 821: `				if(mysql_num_rows($t_result) == 1)`
 * Line 823: `					$t_row = mysql_fetch_array($t_result);`
 * Line 840: `			$t_result = mysql_query(`
 * Line 855: `			if(mysql_num_rows($t_result) > 0)`
 * Line 857: `				while($t_row = mysql_fetch_array($t_result))`
 * Line 882: `				$t_result = mysql_query(`
 * Line 897: `				if((int)mysql_num_rows($t_result) == 1)`
 * Line 972: `			$c_key = mysql_real_escape_string($p_key);`
 * Line 974: `			$t_query = mysql_query("SELECT gm_value`
 * Line 979: `			if(mysql_num_rows($t_query) == 1)`
 * Line 981: `				$t_result_array = mysql_fetch_array($t_query);`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMCat.php
* oldClassConstructors
 * Line 33: `		function GMCat($cPath) `

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMCounter.php
* oldClassConstructors
 * Line 18: `		function GMC() {`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMEbay.php
* oldClassConstructors
 * Line 27: `		function gmEbay($gm_ebay_conf) {`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMGMotion.php
* oldClassConstructors
 * Line 16: `	function GMGMotion()`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMGPrintCartManager.php
* oldClassConstructors
 * Line 17: `	function GMGPrintCartManager()`
* deprecatedFunctions
 * Line 187: `					$c_elements_value = mysql_real_escape_string(stripslashes($t_elements_value));`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMGPrintConfiguration.php
* oldClassConstructors
 * Line 18: `	function GMGPrintConfiguration($p_languages_id)`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMGPrintContentManager.php
* oldClassConstructors
 * Line 14: `	function GMGPrintContentManager()`
* deprecatedFunctions
 * Line 31: `						$c_value = mysql_real_escape_string(stripslashes($p_value));`
 * Line 91: `						$c_value = mysql_real_escape_string(stripslashes($p_value));`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMGPrintElements.php
* oldClassConstructors
 * Line 32: `	function GMGPrintElements($p_elements_id)`
* deprecatedFunctions
 * Line 305: `		$c_type = mysql_real_escape_string(stripslashes($p_type));`
 * Line 349: `						$c_name = mysql_real_escape_string(stripslashes($p_names[$c_languages_id]));`
 * Line 350: `						$c_value = mysql_real_escape_string(stripslashes($t_value));`
 * Line 387: `						$c_name = mysql_real_escape_string(stripslashes($t_name));`
 * Line 449: `							$c_elements_value = mysql_real_escape_string(stripslashes($t_elements_value));`
 * Line 450: `							$c_name = mysql_real_escape_string($t_name);`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMGPrintFileManager.php
* oldClassConstructors
 * Line 14: `	function GMGPrintFileManager()`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMGPrintOrderElements.php
* oldClassConstructors
 * Line 28: `	function GMGPrintOrderElements($p_elements_id)`
* deprecatedFunctions
 * Line 145: `		$c_type = mysql_real_escape_string(stripslashes($p_type));`
 * Line 184: `		$c_name = mysql_real_escape_string(stripslashes($p_name));`
 * Line 206: `		$c_value = mysql_real_escape_string(stripslashes($p_value));`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMGPrintOrderManager.php
* oldClassConstructors
 * Line 14: `	function GMGPrintOrderManager()`
* deprecatedFunctions
 * Line 85: `		$c_name = mysql_real_escape_string(stripslashes($p_name));`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMGPrintOrderSurfaces.php
* oldClassConstructors
 * Line 22: `	function GMGPrintOrderSurfaces($p_surfaces_id)`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMGPrintOrderSurfacesManager.php
* oldClassConstructors
 * Line 20: `	function GMGPrintOrderSurfacesManager($p_surfaces_groups_id)`
* deprecatedFunctions
 * Line 29: `		$c_name = mysql_real_escape_string(stripslashes($p_name));`
 * Line 124: `		$c_name = mysql_real_escape_string(stripslashes($p_name));`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMGPrintProductManager.php
* oldClassConstructors
 * Line 15: `	function GMGPrintProductManager()`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMGPrintSurfaces.php
* oldClassConstructors
 * Line 22: `	function GMGPrintSurfaces($p_surfaces_id)`
* deprecatedFunctions
 * Line 270: `				$c_name = mysql_real_escape_string(stripslashes($t_name));`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMGPrintSurfacesGroupsManager.php
* deprecatedFunctions
 * Line 23: `		$c_name = mysql_real_escape_string(stripslashes($p_name));`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMGPrintSurfacesManager.php
* oldClassConstructors
 * Line 20: `	function GMGPrintSurfacesManager($p_surfaces_groups_id)`
* deprecatedFunctions
 * Line 41: `				$c_name = mysql_real_escape_string(stripslashes($t_name));`
 * Line 244: `		$c_name = mysql_real_escape_string(stripslashes($p_name));`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMGPrintWishlistManager.php
* oldClassConstructors
 * Line 17: `	function GMGPrintWishlistManager()`
* deprecatedFunctions
 * Line 188: `					$c_elements_value = mysql_real_escape_string(stripslashes($t_elements_value));`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMJSON.php
* oldClassConstructors
 * Line 16: `	function GMJSON($p_urlencode = true)`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMJanolaw.php
* oldClassConstructors
 * Line 18: `	function GMJanolaw() `

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMLightboxControl.php
* oldClassConstructors
 * Line 18: `		function GMLightboxControl() {`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMLogoManager.php
* oldClassConstructors
 * Line 25: `		function GMLogoManager($logo_key) {`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMMeta.php
* oldClassConstructors
 * Line 27: `    function GMMeta()`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMProduct.php
* oldClassConstructors
 * Line 26: `		function GMProduct() {`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMSEOBoost.php
* oldClassConstructors
 * Line 25: `    function GMSEOBoost()`
* deprecatedFunctions
 * Line 44: `        $t_result = @mysql_query($t_sql);`
 * Line 45: `        $t_result_array = @mysql_fetch_array($t_result);`
 * Line 91: `										gm_url_keywords = ' . $this->v_binary_string . '"' . mysql_real_escape_string($boosted_name) . '"');`
 * Line 102: `										gm_url_keywords = ' . $this->v_binary_string . '"' . mysql_real_escape_string($boosted_name) . '" AND`
 * Line 104: `            if (mysql_num_rows($result) > 0) {`
 * Line 105: `                $products_id = mysql_result($result, 0, 'products_id');`
 * Line 151: `							SET	gm_url_keywords = "' . mysql_real_escape_string($link_name) . '"`
 * Line 189: `			    SET	products_name = "' . mysql_real_escape_string($productsName) . '"`
 * Line 274: `                                    $c_new_url_keyword = mysql_real_escape_string($t_new_url_keyword);`
 * Line 351: `                                    $c_new_url_keyword = mysql_real_escape_string($t_new_url_keyword);`
 * Line 534: `										gm_url_keywords = ' . $this->v_binary_string . '"' . mysql_real_escape_string($boosted_name) . '"');`
 * Line 545: `										gm_url_keywords = ' . $this->v_binary_string . '"' . mysql_real_escape_string($boosted_name) . '" AND`
 * Line 547: `            if (mysql_num_rows($result) > 0) {`
 * Line 548: `                $categories_id = mysql_result($result, 0, 'categories_id');`
 * Line 572: `									languages_id 	= "' . mysql_real_escape_string($language_id) . '"');`
 * Line 573: `        if (mysql_num_rows($result) == 0) {`
 * Line 576: `            $coID = mysql_result($result, 0, 'content_id');`
 * Line 590: `										gm_url_keywords = ' . $this->v_binary_string . '"' . mysql_real_escape_string($boosted_name) . '"');`
 * Line 601: `										gm_url_keywords = ' . $this->v_binary_string . '"' . mysql_real_escape_string($boosted_name) . '" AND`
 * Line 603: `            if (mysql_num_rows($result) > 0) {`
 * Line 604: `                $coID = mysql_result($result, 0, 'content_group');`
 * Line 637: `            $link_name = 'info-content-' . mysql_real_escape_string($content_id);`
 * Line 642: `							SET	gm_url_keywords = "' . mysql_real_escape_string($link_name) . '"`
 * Line 685: `            $link_name = 'info-content-' . mysql_real_escape_string($content_id);`
 * Line 690: `							SET	gm_url_keywords = "' . mysql_real_escape_string($link_name) . '"`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMSitemap.php
* oldClassConstructors
 * Line 22: `		function GMSitemap() {     `

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMStatusbar.php
* oldClassConstructors
 * Line 15: `		function GMStatusbar() {`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMTSWidget.php
* oldClassConstructors
 * Line 63: `		function GMTSWidget($p_languages_id)`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMTabTokenizerTickets75.php
* oldClassConstructors
 * Line 28: `	function GMTabTokenizerTickets75($content)`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\GMTracker.php
* oldClassConstructors
 * Line 25: `		function GMTracker($type="login") {`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\Tickets75SitemapXML.php
* oldClassConstructors
 * Line 118: `    function Tickets75SitemapXML($ping)`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\csstidy\class.csstidy.php
* oldClassConstructors
 * Line 241: `function csstidy()`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\csstidy\class.csstidy_optimise.php
* oldClassConstructors
 * Line 45: `    function csstidy_optimise(&$css)`

#### C:\Users\marti\Documents\gambio_tickets75\gm\classes\csstidy\class.csstidy_print.php
* oldClassConstructors
 * Line 63: `    function csstidy_print(&$css)`

#### C:\Users\marti\Documents\gambio_tickets75\gm\inc\gm_prepare_string.inc.php
* deprecatedFunctions
 * Line 19: `			if(!gm_magic_check($string)) $string = mysql_real_escape_string($string);`

#### C:\Users\marti\Documents\gambio_tickets75\gm\modules\gm_gprint_admin_application_top.php
* deprecatedFunctions
 * Line 40: `		if(mysql_num_rows($t_get_products_autoindex) == 1){`

#### C:\Users\marti\Documents\gambio_tickets75\gm\properties\controls\PropertiesAdminControl.php
* oldClassConstructors
 * Line 13: `	function PropertiesAdminControl() `

#### C:\Users\marti\Documents\gambio_tickets75\gm\properties\controls\PropertiesBasket.php
* oldClassConstructors
 * Line 15: `	function PropertiesBasket() `

#### C:\Users\marti\Documents\gambio_tickets75\gm\properties\controls\PropertiesCombisAdminControl.php
* oldClassConstructors
 * Line 13: `	function PropertiesCombisAdminControl() `

#### C:\Users\marti\Documents\gambio_tickets75\gm\properties\controls\PropertiesControl.php
* oldClassConstructors
 * Line 15: `	function PropertiesControl() `

#### C:\Users\marti\Documents\gambio_tickets75\gm\properties\data\ProductPropertiesData.php
* oldClassConstructors
 * Line 20: `	function ProductPropertiesData($p_products_id, $p_language_id) `

#### C:\Users\marti\Documents\gambio_tickets75\gm\properties\data\PropertiesCombisStructSupplier.php
* oldClassConstructors
 * Line 13: `	function PropertiesCombisStructSupplier()`

#### C:\Users\marti\Documents\gambio_tickets75\gm\properties\data\PropertiesDataAgent.php
* oldClassConstructors
 * Line 13: `	function PropertiesDataAgent() `
* deprecatedFunctions
 * Line 210: `				$t_details_array['products_vpe_name'] = mysql_result($t_result, 0, 'products_vpe_name');`

#### C:\Users\marti\Documents\gambio_tickets75\gm\properties\data\PropertiesStructSupplier.php
* oldClassConstructors
 * Line 13: `	function PropertiesStructSupplier()`

#### C:\Users\marti\Documents\gambio_tickets75\gm\properties\page_modules\PropertiesAdminView.php
* oldClassConstructors
 * Line 21: `	function PropertiesAdminView($p_get_array, $p_post_array) `

#### C:\Users\marti\Documents\gambio_tickets75\gm\properties\page_modules\PropertiesCombisAdminView.php
* oldClassConstructors
 * Line 21: `	function PropertiesCombisAdminView($p_get_array, $p_post_array) `

#### C:\Users\marti\Documents\gambio_tickets75\gm\properties\page_modules\PropertiesView.php
* oldClassConstructors
 * Line 67: `	function PropertiesView($p_get_array=false, $p_post_array=false) `

#### C:\Users\marti\Documents\gambio_tickets75\gm_ajax.php
* deprecatedFunctions
 * Line 65: `//mysql_close();`

#### C:\Users\marti\Documents\gambio_tickets75\gm_gprint.js.php
* deprecatedFunctions
 * Line 33: `	mysql_close();`

#### C:\Users\marti\Documents\gambio_tickets75\heidelpay\HeidelPayOrderManipulator.php
* deprecatedFunctions
 * Line 72: `        $stat = mysql_affected_rows($db_link);`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\IclearAddress.php
* oldClassConstructors
 * Line 42: `  function IclearAddress(&$icCore) {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\IclearBasket.php
* oldClassConstructors
 * Line 64: `	function IclearBasket(&$icCore) {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\IclearCore.php
* newOperatorWithReference
 * Line 252: `        $rv =& new $class($this);`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\IclearSOAP.php
* oldClassConstructors
 * Line 42: `	  function IclearSOAP(&$icCore) {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\IclearSoapClient.nusoap.php
* oldClassConstructors
 * Line 27: `  function IclearSoapClient(&$icCore) {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\IclearSoapClient.php5.php
* oldClassConstructors
 * Line 41: `  function IclearSoapClient(&$icCore) {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\IclearSoapServer.nusoap.php
* oldClassConstructors
 * Line 30: `  function IclearSoapServer(&$icCore) {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\class\IclearAddress.php
* oldClassConstructors
 * Line 42: `  function IclearAddress(&$icCore) {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\class\IclearBase.php
* oldClassConstructors
 * Line 32: `	function IclearBase(&$icCore) {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\class\IclearBasket.php
* oldClassConstructors
 * Line 46: `	function IclearBasket(&$icCore) {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\class\IclearCore.php
* oldClassConstructors
 * Line 120: `	function IclearCore($icLang = false) {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\class\IclearError.php
* oldClassConstructors
 * Line 29: `	function IclearError() {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\class\IclearSOAP.php
* oldClassConstructors
 * Line 40: `	function IclearSOAP(&$icCore) {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\class\IclearSoapClient.nusoap.php
* oldClassConstructors
 * Line 26: `	function IclearSoapClient(&$icCore) {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\class\IclearSoapClient.php5.php
* oldClassConstructors
 * Line 39: `	function IclearSoapClient(&$icCore) {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\class\IclearSoapServer.nusoap.php
* oldClassConstructors
 * Line 27: `	function IclearSoapServer(&$icCore) {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\class\IclearSoapServer.php5.php
* oldClassConstructors
 * Line 27: `	function IclearSoapServer(&$icCore) {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\class\IclearUpdate.php
* oldClassConstructors
 * Line 29: `	function IclearUpdate(&$icCore) {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\class\IclearWrapperBase.php
* oldClassConstructors
 * Line 38: `	function IclearWrapperBase(&$icCore) {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\lib\nusoap\class.nusoap_base.php
* oldClassConstructors
 * Line 199: `	function nusoap_base() {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\lib\nusoap\class.soap_fault.php
* oldClassConstructors
 * Line 43: `	function nusoap_fault($faultcode,$faultactor='',$faultstring='',$faultdetail=''){`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\lib\nusoap\class.soap_parser.php
* oldClassConstructors
 * Line 54: `	function nusoap_parser($xml,$encoding='UTF-8',$method='',$decode_utf8=true){`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\lib\nusoap\class.soap_server.php
* oldClassConstructors
 * Line 165: `	function nusoap_server($wsdl=false){`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\lib\nusoap\class.soap_transport_http.php
* oldClassConstructors
 * Line 54: `	function soap_transport_http($url, $curl_options = NULL, $use_curl = false){`
* deprecatedFunctions
 * Line 536: `			//set_magic_quotes_runtime(0);`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\lib\nusoap\class.soap_val.php
* oldClassConstructors
 * Line 67: `  	function soapval($name='soapval',$type=false,$value=-1,$element_ns=false,$type_ns=false,$attributes=false) {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\lib\nusoap\class.soapclient.php
* oldClassConstructors
 * Line 91: `	function nusoap_client($endpoint,$wsdl = false,$proxyhost = false,$proxyport = false,$proxyusername = false, $proxypassword = false, $timeout = 0, $response_timeout = 30, $portName = ''){`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\lib\nusoap\class.wsdl.php
* oldClassConstructors
 * Line 67: `    function wsdl($wsdl = '',$proxyhost=false,$proxyport=false,$proxyusername=false,$proxypassword=false,$timeout=0,$response_timeout=30,$curl_options=null,$use_curl=false){`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\lib\nusoap\class.wsdlcache.php
* oldClassConstructors
 * Line 44: `	function nusoap_wsdlcache($cache_dir='.', $cache_lifetime=0) {`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\lib\nusoap\class.xmlschema.php
* oldClassConstructors
 * Line 50: `	function nusoap_xmlschema($schema='',$xml='',$namespaces=array()){`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\lib\nusoap\nusoap.php
* oldClassConstructors
 * Line 199: `	function nusoap_base() {`
 * Line 976: `	function nusoap_fault($faultcode,$faultactor='',$faultstring='',$faultdetail=''){`
 * Line 1063: `	function nusoap_xmlschema($schema='',$xml='',$namespaces=array()){`
 * Line 2022: `  	function soapval($name='soapval',$type=false,$value=-1,$element_ns=false,$type_ns=false,$attributes=false) {`
 * Line 2104: `	function soap_transport_http($url, $curl_options = NULL, $use_curl = false){`
 * Line 3462: `	function nusoap_server($wsdl=false){`
 * Line 4449: `    function wsdl($wsdl = '',$proxyhost=false,$proxyport=false,$proxyusername=false,$proxypassword=false,$timeout=0,$response_timeout=30,$curl_options=null,$use_curl=false){`
 * Line 6331: `	function nusoap_parser($xml,$encoding='UTF-8',$method='',$decode_utf8=true){`
 * Line 6985: `	function nusoap_client($endpoint,$wsdl = false,$proxyhost = false,$proxyport = false,$proxyusername = false, $proxypassword = false, $timeout = 0, $response_timeout = 30, $portName = ''){`
* deprecatedFunctions
 * Line 2586: `			//set_magic_quotes_runtime(0);`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\lib\nusoap.php
* oldClassConstructors
 * Line 181: `	function nusoap_base() {`
 * Line 886: `	function soap_fault($faultcode,$faultactor='',$faultstring='',$faultdetail=''){`
 * Line 968: `	function XMLSchema($schema='',$xml='',$namespaces=array()){`
 * Line 1849: `  	function soapval($name='soapval',$type=false,$value=-1,$element_ns=false,$type_ns=false,$attributes=false) {`
 * Line 1920: `	function soap_transport_http($url){`
 * Line 2983: `	function soap_server($wsdl=false){`
 * Line 3870: `    function wsdl($wsdl = '',$proxyhost=false,$proxyport=false,$proxyusername=false,$proxypassword=false,$timeout=0,$response_timeout=30){`
 * Line 5545: `	function soap_parser($xml,$encoding='UTF-8',$method='',$decode_utf8=true){`
 * Line 6163: `	function nusoapclient($endpoint,$wsdl = false,$proxyhost = false,$proxyport = false,$proxyusername = false, $proxypassword = false, $timeout = 0, $response_timeout = 30){`
* deprecatedFunctions
 * Line 2230: `			set_magic_quotes_runtime(0);`
* newOperatorWithReference
 * Line 6183: `				$this->wsdl =& new wsdl($this->wsdlFile,$this->proxyhost,$this->proxyport,$this->proxyusername,$this->proxypassword,$this->timeout,$this->response_timeout);`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\wrappers\osc22ms1.php
* oldClassConstructors
 * Line 60: `	function IclearWrapper(&$icCore) {`
* variableInterpolation
 * Line 628: `					//tep_db_prepare_input($order->$prefix[$key])`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\wrappers\xtc304.base.php
* oldClassConstructors
 * Line 133: `	function IclearWrapperXTC(&$icCore) {`
* variableInterpolation
 * Line 499: `					//xtc_db_prepare_input($order->$prefix[$key])`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\wrappers\xtc304sp1.php
* oldClassConstructors
 * Line 27: `	function IclearWrapper(&$icCore) {`

#### C:\Users\marti\Documents\gambio_tickets75\import_tel_codes.php
* deprecatedFunctions
 * Line 16: `$link = mysql_connect('localhost', 'root', '');`
 * Line 18: `	    die('Keine Verbindung möglich: ' . mysql_error());`
 * Line 20: `	mysql_select_db('tickets75');`
 * Line 22: `	$result = mysql_query("SELECT * FROM countries");`
 * Line 23: `	while($row = mysql_fetch_assoc($result)){`
 * Line 31: `				mysql_query("UPDATE countries SET countries_telephone_prefix = '00".$key."' WHERE countries_iso_code_2 = '".$row['countries_iso_code_2']."'");`
 * Line 33: `				mysql_query("UPDATE countries SET countries_telephone_prefix = '' WHERE countries_iso_code_2 = '".$row['countries_iso_code_2']."'");`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_db_close.inc.php
* variableInterpolation
 * Line 16: `    global $$link;`
* deprecatedFunctions
 * Line 17: `    return mysql_close($$link);`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_db_connect.inc.php
* variableInterpolation
 * Line 18: `    global $$link;`
* deprecatedFunctions
 * Line 20: `     	$$link = @mysql_pconnect($server, $username, $password);`
 * Line 22: `		$$link = @mysql_connect($server, $username, $password);`
 * Line 25: `    $vers = @mysql_get_server_info();`
 * Line 26: `    if(substr($vers,0,1) > 4) @mysql_query("SET SESSION sql_mode=''");`
 * Line 28: `    if ($$link) @mysql_select_db($database);`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_db_connect_installer.inc.php
* variableInterpolation
 * Line 19: `    global $$link, $db_error;`
* deprecatedFunctions
 * Line 25: `    $$link = @mysql_connect($server, $username, $password) or $db_error = mysql_error();`
 * Line 28: `    $vers = @mysql_get_server_info();`
 * Line 29: `    if(substr($vers,0,1) > 4) @mysql_query("SET SESSION sql_mode=''");`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_db_data_seek.inc.php
* deprecatedFunctions
 * Line 20: `         if (!is_array($db_query)) return mysql_data_seek($db_query, $row_number);`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_db_fetch_array.inc.php
* deprecatedFunctions
 * Line 26: `    return mysql_fetch_array($db_query, MYSQL_ASSOC);`
 * Line 50: `		//var_dump(mysql_fetch_array($db_query, MYSQL_ASSOC));`
 * Line 51: `		return mysql_fetch_array($db_query, MYSQL_ASSOC);`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_db_fetch_array_utf8.inc.php
* deprecatedFunctions
 * Line 26: `    return mysql_fetch_array($db_query, MYSQL_ASSOC);`
 * Line 50: `		return mysql_fetch_array($db_query, MYSQL_ASSOC);`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_db_fetch_fields.inc.php
* deprecatedFunctions
 * Line 16: `    return mysql_fetch_field($db_query);`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_db_free_result.inc.php
* deprecatedFunctions
 * Line 16: `    return mysql_free_result($db_query);`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_db_input.inc.php
* variableInterpolation
 * Line 16: `  global $$link;`
* deprecatedFunctions
 * Line 18: `    return mysql_real_escape_string($string, $$link);`
 * Line 20: `    return mysql_escape_string($string);`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_db_insert_id.inc.php
* deprecatedFunctions
 * Line 16: `    return mysql_insert_id();`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_db_install.inc.php
* deprecatedFunctions
 * Line 24: `        $db_error = mysql_error();`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_db_num_rows.inc.php
* deprecatedFunctions
 * Line 21: `         if (!is_array($db_query)) return mysql_num_rows($db_query);`
 * Line 24: `    if (!is_array($db_query)) return mysql_num_rows($db_query);`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_db_query.inc.php
* variableInterpolation
 * Line 21: `	global $$link;`
* deprecatedFunctions
 * Line 53: `			@mysql_data_seek($result, 0);`
 * Line 58: `			$result = mysql_query($query, $$link) or xtc_db_error($query, mysql_errno(), mysql_error());`
 * Line 66: `		$result = mysql_query($query, $$link) or xtc_db_error($query, mysql_errno(), mysql_error());`
 * Line 70: `		$result_error = mysql_error();`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_db_queryCached.inc.php
* variableInterpolation
 * Line 13: `    global $$link;`
* deprecatedFunctions
 * Line 29: `        $result = mysql_query($query, $$link) or xtc_db_error($query, mysql_errno(), mysql_error());`
 * Line 31: `                $result_error = mysql_error();`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_db_query_installer.inc.php
* variableInterpolation
 * Line 16: `    global $$link;`
* deprecatedFunctions
 * Line 17: `    return mysql_query($query, $$link);`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_db_select_db.inc.php
* deprecatedFunctions
 * Line 16: `    return mysql_select_db($database);`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_db_test_connection.inc.php
* deprecatedFunctions
 * Line 20: `        $db_error = mysql_error();`
 * Line 23: `          $db_error = mysql_error();`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_db_test_create_db_permission.inc.php
* deprecatedFunctions
 * Line 29: `          $db_error = mysql_error();`
 * Line 36: `        $db_error = mysql_error();`
 * Line 45: `                  $db_error = mysql_error();`
 * Line 49: `              $db_error = mysql_error();`
 * Line 52: `            $db_error = mysql_error();`
 * Line 55: `          $db_error = mysql_error();`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_get_db_cache.inc.php
* deprecatedFunctions
 * Line 27: `//      $conn = mysql_connect("localhost", "apachecon", "apachecon");`
 * Line 29: `//      if ($err = mysql_error()) trigger_error($err, E_USER_ERROR);`

#### C:\Users\marti\Documents\gambio_tickets75\inc\xtc_sqlSafeString.inc.php
* deprecatedFunctions
 * Line 16: `    return (NULL === $param ? "NULL" : '"' . mysql_escape_string($param) . '"');`

#### C:\Users\marti\Documents\gambio_tickets75\includes\application_bottom.php
* deprecatedFunctions
 * Line 167: `    mysql_close();`

#### C:\Users\marti\Documents\gambio_tickets75\includes\application_bottom_old.php
* deprecatedFunctions
 * Line 126: `mysql_close();`

#### C:\Users\marti\Documents\gambio_tickets75\includes\application_top.php
* deprecatedFunctions
 * Line 177: `mysql_query("SET NAMES 'utf8'");`
 * Line 178: `mysql_query("SET CHARACTER SET utf8");`
 * Line 179: `mysql_query("SET SESSION collation_connection = 'utf8_unicode_ci'");`
 * Line 488: `            mysql_close();`
 * Line 503: `            mysql_close();`
 * Line 518: `            mysql_close();`
 * Line 565: `                mysql_close();`
 * Line 813: `                mysql_close();`

#### C:\Users\marti\Documents\gambio_tickets75\includes\application_top_min.php
* deprecatedFunctions
 * Line 168: `mysql_query("SET NAMES 'utf8'");`
 * Line 169: `mysql_query("SET CHARACTER SET utf8");`
 * Line 170: `mysql_query("SET SESSION collation_connection = 'utf8_unicode_ci'");`
 * Line 459: `			mysql_close();`
 * Line 474: `			mysql_close();`
 * Line 489: `			mysql_close();`
 * Line 536: `				mysql_close();`
 * Line 708: `				mysql_close();`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\Smarty_2.6.14\Config_File.class.php
* oldClassConstructors
 * Line 64: `    function Config_File($config_path = NULL)`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\Smarty_2.6.14\Smarty.class.php
* oldClassConstructors
 * Line 501: `    function Smarty()`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\Smarty_2.6.14\Smarty_Compiler.class.php
* oldClassConstructors
 * Line 75: `    function Smarty_Compiler()`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\class.heidelpay.php
* oldClassConstructors
 * Line 26: `	function heidelpay()/*{{{*/`
* deprecatedFunctions
 * Line 516: `		$stat = mysql_affected_rows($db_link);`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\class.inputfilter.php
* deprecatedFunctions
 * Line 343: `			mysql_escape_string($string);`
 * Line 346: `			mysql_real_escape_string($string);`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\class.mapa.php
* oldClassConstructors
 * Line 24: `  function mapa()/*{{{*/`
* deprecatedFunctions
 * Line 432: `    $stat = mysql_affected_rows($db_link);`
 * Line 565: `    return mysql_affected_rows($db_link);`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\class.moneybookers.php
* oldClassConstructors
 * Line 43: `	function fcnt_moneybookers(){`
* deprecatedFunctions
 * Line 229: `		} while (mysql_num_rows($result));`
 * Line 258: `		$tables = mysql_list_tables(DB_DATABASE);`
 * Line 259: `		while ($row = mysql_fetch_row($tables)) {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\class.phpmailer.php
* deprecatedFunctions
 * Line 962: `        $magic_quotes = get_magic_quotes_runtime();`
 * Line 963: `        set_magic_quotes_runtime(0);`
 * Line 967: `        set_magic_quotes_runtime($magic_quotes);`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\class.smtp.php
* oldClassConstructors
 * Line 54: `    function SMTP() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\main.php
* oldClassConstructors
 * Line 17: ` 	function main () {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\order.php
* oldClassConstructors
 * Line 41: `    function order($order_id = '')`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\order_total.php
* oldClassConstructors
 * Line 180: `	function order_total() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\payment.php
* oldClassConstructors
 * Line 34: `	function payment($module = '', $mode = null,$hasOrder = false)`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\paypal_checkout.php
* oldClassConstructors
 * Line 54: `	function paypal_checkout() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\product.php
* oldClassConstructors
 * Line 26: `	function product($pID = 0,$arrayOfFields=array()) {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\secupay_api.php
* oldClassConstructors
 * Line 141: `	function secupay_log($log) {`
 * Line 168: `		function secupay_api($params, $function = "debitguarantee", $format ="json") {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\session\MysqlSessionHandler.php
* deprecatedFunctions
 * Line 54: `        if(!@mysql_ping()) {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\shipping.php
* oldClassConstructors
 * Line 21: `    function shipping($module = '') {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\shopping_cart.php
* oldClassConstructors
 * Line 37: `	function shoppingCart() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\vat_validation.php
* oldClassConstructors
 * Line 17: `	function vat_validation($vat_id = '', $customers_id = '', $customers_status = '', $country_id = '', $guest = false) {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\wish_list.php
* oldClassConstructors
 * Line 36: `	function wishList() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\xmlparserv4.php
* oldClassConstructors
 * Line 19: `    function XMLParser($xml){`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\xtcPrice.php
* oldClassConstructors
 * Line 20: `    function xtcPrice($currency, $cGroup) {`
* duplicateFunctionParameter
 * Line 280: `    function xtcShowNote($vpeStatus, $vpeStatus = 0) {`
 * Line 390: `    function xtcFormatSpecialGraduated($pID, $sPrice, $pPrice, $format, $vpeStatus = 0, $pID) {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\iclear\iclear_wsdl.php
* oldClassConstructors
 * Line 72: `  function iclearWSDL($type, $shopID = '', $sessionID = '', $user = '', $pass = '') {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\iclear\nusoap.php
* oldClassConstructors
 * Line 188: `	function nusoap_base() {`
 * Line 893: `	function soap_fault($faultcode,$faultactor='',$faultstring='',$faultdetail=''){`
 * Line 975: `	function XMLSchema($schema='',$xml='',$namespaces=array()){`
 * Line 1856: `  	function soapval($name='soapval',$type=false,$value=-1,$element_ns=false,$type_ns=false,$attributes=false) {`
 * Line 1927: `	function soap_transport_http($url){`
 * Line 2990: `	function soap_server($wsdl=false){`
 * Line 3877: `    function wsdl($wsdl = '',$proxyhost=false,$proxyport=false,$proxyusername=false,$proxypassword=false,$timeout=0,$response_timeout=30){`
 * Line 5552: `	function soap_parser($xml,$encoding='UTF-8',$method='',$decode_utf8=true){`
 * Line 6170: `	function nusoapclient($endpoint,$wsdl = false,$proxyhost = false,$proxyport = false,$proxyusername = false, $proxypassword = false, $timeout = 0, $response_timeout = 30){`
* deprecatedFunctions
 * Line 2237: `			set_magic_quotes_runtime(0);`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\error_handler.php
* deprecatedFunctions
 * Line 31: `                WHERE cd.gm_url_keywords = '".mysql_real_escape_string($url)."' `

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\order_total\ot_coupon.php
* oldClassConstructors
 * Line 28: `	function ot_coupon() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\order_total\ot_gambioultra.php
* deprecatedFunctions
 * Line 42: `				$result = mysql_query('`
 * Line 55: `				//echo mysql_error();`
 * Line 56: `				if(mysql_errno() == 0)  {`
 * Line 57: `					while(($row = mysql_fetch_array($result) )) {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\order_total\ot_gv.php
* oldClassConstructors
 * Line 28: `	function ot_gv() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\order_total\ot_sofort.php
* oldClassConstructors
 * Line 29: `	function ot_sofort() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\amoneybookers.php
* oldClassConstructors
 * Line 27: `	function amoneybookers() {`
* deprecatedFunctions
 * Line 62: `			while (list ($currID) = mysql_fetch_row($result)) {`
 * Line 66: `			while (list ($currID) = mysql_fetch_row($result)) {`
 * Line 177: `		list ($lang_code) = mysql_fetch_row($result);`
 * Line 190: `		list ($mbCountry) = mysql_fetch_row($result);`
 * Line 530: `			while (list ($currID) = mysql_fetch_row($result)) {`
 * Line 534: `			while (list ($currID) = mysql_fetch_row($result)) {`
 * Line 546: `		$tables = mysql_list_tables(DB_DATABASE);`
 * Line 547: `		while ($row = mysql_fetch_row($tables)) {`
 * Line 618: `		} while (mysql_num_rows($result));`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\cash.php
* oldClassConstructors
 * Line 16: `	function cash() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\cc.php
* oldClassConstructors
 * Line 21: `	function cc() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\clickandbuy_v2.php
* oldClassConstructors
 * Line 48: `  function clickandbuy_v2()`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\cod.php
* oldClassConstructors
 * Line 19: `	function cod() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\eustandardtransfer.php
* oldClassConstructors
 * Line 19: `	function eustandardtransfer() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\hpcc.php
* oldClassConstructors
 * Line 10: `	function hpcc() /*{{{*/`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\hpdc.php
* oldClassConstructors
 * Line 10: `	function hpdc() /*{{{*/`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\hpdd.php
* oldClassConstructors
 * Line 10: `	function hpdd() /*{{{*/`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\hpeps.php
* oldClassConstructors
 * Line 10: `  function hpeps() /*{{{*/`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\hpgp.php
* oldClassConstructors
 * Line 10: `	function hpgp() /*{{{*/`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\hpidl.php
* oldClassConstructors
 * Line 10: `	function hpidl() /*{{{*/`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\hpinfo.php
* oldClassConstructors
 * Line 10: `	function hpinfo() /*{{{*/`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\hppp.php
* oldClassConstructors
 * Line 10: `  function hppp() /*{{{*/`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\hpppal.php
* oldClassConstructors
 * Line 10: `  function hpppal() /*{{{*/`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\hpsu.php
* oldClassConstructors
 * Line 10: `  function hpsu() /*{{{*/`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\invoice.php
* oldClassConstructors
 * Line 16: `	function invoice() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\luupws.php
* oldClassConstructors
 * Line 18: `    function luupws() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\mapacc.php
* oldClassConstructors
 * Line 10: `  function mapacc() /*{{{*/`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\mapadc.php
* oldClassConstructors
 * Line 10: `  function mapadc() /*{{{*/`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\mapadd.php
* oldClassConstructors
 * Line 10: `  function mapadd() /*{{{*/`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\mapaeps.php
* oldClassConstructors
 * Line 10: `  function mapaeps() /*{{{*/`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\mapagp.php
* oldClassConstructors
 * Line 10: `  function mapagp() /*{{{*/`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\mapaidl.php
* oldClassConstructors
 * Line 10: `  function mapaidl() /*{{{*/`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\mapappal.php
* oldClassConstructors
 * Line 10: `  function mapappal() /*{{{*/`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\mapasu.php
* oldClassConstructors
 * Line 10: `  function mapasu() /*{{{*/`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\masterpayment\MasterpaymentActions.class.php
* deprecatedFunctions
 * Line 85: `				$num_check = mysql_num_rows($check_query);`
 * Line 130: `			$num_check = mysql_num_rows($check_payment);`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\masterpayment\MasterpaymentCallback.class.php
* oldClassConstructors
 * Line 29: `	function MasterpaymentCallback(&$_var)`
* deprecatedFunctions
 * Line 81: `		$check_order = xtc_db_query("select count(orders_id) as a_orders from " . TABLE_ORDERS . " where orders_id = '".mysql_escape_string($this->order_ID)."' limit 1");`
 * Line 194: `		$select_customerid = xtc_db_query("select customers_id from " . TABLE_ORDERS . " where orders_id = '".mysql_escape_string($this->order_ID)."' limit 1");`
 * Line 205: `		$select_olanguage_query = xtc_db_query("select language from " . TABLE_ORDERS . " where orders_id = '".mysql_escape_string($this->order_ID)."'");`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\masterpayment\MasterpaymentRequest.class.php
* deprecatedFunctions
 * Line 59: `		$check_order = xtc_db_query("select count(orders_id) as a_orders from " . TABLE_ORDERS . " where orders_id = '".mysql_escape_string($this->order_ID)."' limit 1");`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\masterpayment\masterpayment_actions.class.php
* oldClassConstructors
 * Line 29: `	function masterpayment_actions()`
* deprecatedFunctions
 * Line 79: `			$num_check = mysql_num_rows($check_query);`
 * Line 124: `			$num_check = mysql_num_rows($check_payment);`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\masterpayment\masterpayment_callback.class.php
* deprecatedFunctions
 * Line 58: `		$check_order = xtc_db_query("select count(orders_id) as a_orders from " . TABLE_ORDERS . " where orders_id = '".mysql_escape_string($this->order_ID)."' limit 1");`
 * Line 191: `		$select_customerid = xtc_db_query("select customers_id from " . TABLE_ORDERS . " where orders_id = '".mysql_escape_string($this->order_ID)."' limit 1");`
 * Line 201: `		$select_olanguage_query = xtc_db_query("select language from " . TABLE_ORDERS . " where orders_id = '".mysql_escape_string($this->order_ID)."'");`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\masterpayment\masterpayment_request.class.php
* deprecatedFunctions
 * Line 59: `		$check_order = xtc_db_query("select count(orders_id) as a_orders from " . TABLE_ORDERS . " where orders_id = '".mysql_escape_string($this->order_ID)."' limit 1");`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\moneybookers.php
* oldClassConstructors
 * Line 21: `	function moneybookers() {`
* deprecatedFunctions
 * Line 33: `		while (list ($currID) = mysql_fetch_row($result)) {`
 * Line 37: `		while (list ($currID) = mysql_fetch_row($result)) {`
 * Line 41: `		list ($this->defCurr) = mysql_fetch_row($result);`
 * Line 43: `		list ($this->defLang) = mysql_fetch_row($result);`
 * Line 93: `		list ($lang_code) = mysql_fetch_row($result);`
 * Line 106: `		list ($mbCountry) = mysql_fetch_row($result);`
 * Line 262: `		} while (mysql_num_rows($result));`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\moneybookers_cc.php
* oldClassConstructors
 * Line 34: `	function moneybookers_cc() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\moneybookers_cgb.php
* oldClassConstructors
 * Line 34: `	function moneybookers_cgb() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\moneybookers_csi.php
* oldClassConstructors
 * Line 34: `	function moneybookers_csi() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\moneybookers_elv.php
* oldClassConstructors
 * Line 34: `	function moneybookers_elv() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\moneybookers_giropay.php
* oldClassConstructors
 * Line 34: `	function moneybookers_giropay() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\moneybookers_ideal.php
* oldClassConstructors
 * Line 34: `	function moneybookers_ideal() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\moneybookers_mae.php
* oldClassConstructors
 * Line 34: `	function moneybookers_mae() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\moneybookers_netpay.php
* oldClassConstructors
 * Line 34: `	function moneybookers_netpay() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\moneybookers_psp.php
* oldClassConstructors
 * Line 34: `	function moneybookers_psp() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\moneybookers_pwy.php
* oldClassConstructors
 * Line 34: `	function moneybookers_pwy() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\moneybookers_sft.php
* oldClassConstructors
 * Line 34: `	function moneybookers_sft() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\moneybookers_wlt.php
* oldClassConstructors
 * Line 34: `	function moneybookers_wlt() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\moneyorder.php
* oldClassConstructors
 * Line 19: `	function moneyorder() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\paypal.php
* oldClassConstructors
 * Line 31: `	function paypal() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\paypalexpress.php
* oldClassConstructors
 * Line 31: `	function paypalexpress() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\paypalgambio_alt.php
* oldClassConstructors
 * Line 19: `	function paypalgambio_alt() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\pn_sofortueberweisung.php
* oldClassConstructors
 * Line 40: `	function pn_sofortueberweisung () {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\qpay.php
* deprecatedFunctions
 * Line 34: `        list($lang_code) = mysql_fetch_row($result);`
 * Line 60: `        $consumerInformation = mysql_fetch_assoc($result);`
 * Line 267: `        $resultRow = mysql_fetch_row($result);`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\qpayccard.php
* oldClassConstructors
 * Line 6: `    function qpayccard() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\qpayccardmoto.php
* oldClassConstructors
 * Line 6: `    function qpayccardmoto() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\qpayelv.php
* oldClassConstructors
 * Line 6: `    function qpayelv() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\qpayeps.php
* oldClassConstructors
 * Line 6: `    function qpayeps() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\qpaygiropay.php
* oldClassConstructors
 * Line 6: `    function qpaygiropay() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\qpayidl.php
* oldClassConstructors
 * Line 6: `    function qpayidl() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\qpaymaestro.php
* oldClassConstructors
 * Line 6: `    function qpaymaestro() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\qpaypaypal.php
* oldClassConstructors
 * Line 6: `    function qpaypaypal() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\qpaypbx.php
* oldClassConstructors
 * Line 6: `    function qpaypbx() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\qpaypsc.php
* oldClassConstructors
 * Line 6: `    function qpaypsc() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\qpayquick.php
* oldClassConstructors
 * Line 6: `    function qpayquick() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\qpayselect.php
* oldClassConstructors
 * Line 6: `    function qpayselect() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\saferpaygw.php
* oldClassConstructors
 * Line 23: `	function saferpaygw() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\secupay_kk_xtc.php
* oldClassConstructors
 * Line 19: `	function secupay_kk_xtc() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\secupay_ls_xtc.php
* oldClassConstructors
 * Line 15: `	function secupay_ls_xtc() {`
* deprecatedFunctions
 * Line 304: `		xtc_db_query("update " . TABLE_ORDERS . " set comments='" . mysql_real_escape_string($paymethod) . "' where orders_id=$insert_id ");`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\sofort_ideal.php
* deprecatedFunctions
 * Line 450: `						$result = mysql_query('`
 * Line 456: `						while(($row = mysql_fetch_array($result) )) {`
 * Line 458: `							mysql_query('`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\sofort_sofortrechnung.php
* variableInterpolation
 * Line 359: `			global $$shippingModule; //notice $$`
* deprecatedFunctions
 * Line 620: `		$resProd = mysql_query("SELECT	orders_products_id,`
 * Line 625: `		while($rowProd = mysql_fetch_array($resProd)){`
 * Line 627: `			$resAttr = mysql_query("SELECT	products_options,`
 * Line 633: `			if(mysql_num_rows($resAttr) >= 1) {`
 * Line 634: `				while($rowAttr = mysql_fetch_array($resAttr)) {`
 * Line 635: `					$resOpt = mysql_query(" SELECT	products_options_id`
 * Line 639: `					$rowOpt = mysql_fetch_array($resOpt);`
 * Line 640: `					$resOptVal = mysql_query("	SELECT	products_options_values_id`
 * Line 645: `					while($rowOptVal = mysql_fetch_array($resOptVal)){`
 * Line 646: `						$resCheck = mysql_query("SELECT	products_options_values_to_products_options_id`
 * Line 651: `						if (mysql_num_rows($resCheck) == 1){`
 * Line 659: `			mysql_query("INSERT INTO sofort_products (orders_id, orders_products_id, item_id) VALUES ('".(int)$ordersId."','".HelperFunctions::escapeSql($rowProd['orders_products_id'])."','".HelperFunctions::escapeSql($itemId)."')");`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\vrepay_elv.php
* oldClassConstructors
 * Line 17: `	function vrepay_elv() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\vrepay_giropay.php
* oldClassConstructors
 * Line 17: `	function vrepay_giropay() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\vrepay_kreditkarte.php
* oldClassConstructors
 * Line 17: `	function vrepay_kreditkarte() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\payment\worldpay.php
* oldClassConstructors
 * Line 40: `	function worldpay() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\shipping\etix.php
* oldClassConstructors
 * Line 21: `    function etix()`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\shipping\gambioultra.php
* deprecatedFunctions
 * Line 138: `				$result = mysql_query('`
 * Line 151: `				//echo mysql_error();`
 * Line 152: `				if(mysql_errno() == 0)  {`
 * Line 153: `					while(($row = mysql_fetch_array($result) )) {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\shipping\interkurier.php
* deprecatedFunctions
 * Line 139: `$last = mysql_fetch_object($lastNumber);`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\shipping\selfpickup.php
* oldClassConstructors
 * Line 21: `    function selfpickup()`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\shipping\zones.php
* oldClassConstructors
 * Line 110: `    function zones() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\modules\yatego\CYExportYatego.php
* oldClassConstructors
 * Line 25: `	function CYExportYatego($mode) {`
* deprecatedFunctions
 * Line 53: `		if(mysql_num_rows(mysql_query("SHOW COLUMNS FROM products LIKE 'products_ean'")) > 0) `
 * Line 57: `		if(mysql_num_rows(mysql_query("SHOW COLUMNS FROM products LIKE 'manufacturers_id'")) > 0) `
 * Line 206: `		while($row = mysql_fetch_assoc($result)) `
 * Line 228: `			if(mysql_num_rows(mysql_query("SHOW COLUMNS FROM products LIKE 'products_ean'")) > 0)`
 * Line 232: `			if(mysql_num_rows(mysql_query("SHOW COLUMNS FROM products LIKE 'manufacturers_id'")) > 0) `
 * Line 259: `			if(mysql_num_rows(mysql_query("SHOW COLUMNS FROM products LIKE 'products_ean'")) > 0) `
 * Line 263: `			if(mysql_num_rows(mysql_query("SHOW COLUMNS FROM products LIKE 'manufacturers_id'")) > 0) `
 * Line 319: `		while($articleLine = mysql_fetch_assoc($result)) {`
 * Line 415: `		while($variantSetsLine = mysql_fetch_assoc($result)) {`
 * Line 443: `		while($variantsLine = mysql_fetch_assoc($result)) {`
 * Line 470: `		while($categoriesLine = mysql_fetch_assoc($result)) {`
 * Line 498: `		while($stocksLine = mysql_fetch_assoc($result)) {`
 * Line 541: `		while($discountSetsLine = mysql_fetch_assoc($result)) {`
 * Line 562: `		while($discountsLine = mysql_fetch_assoc($result)) {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\nusoap\lib\class.nusoap_base.php
* oldClassConstructors
 * Line 182: `	function nusoap_base() {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\nusoap\lib\class.soap_fault.php
* oldClassConstructors
 * Line 43: `	function soap_fault($faultcode,$faultactor='',$faultstring='',$faultdetail=''){`

#### C:\Users\marti\Documents\gambio_tickets75\includes\nusoap\lib\class.soap_parser.php
* oldClassConstructors
 * Line 52: `	function soap_parser($xml,$encoding='UTF-8',$method='',$decode_utf8=true){`

#### C:\Users\marti\Documents\gambio_tickets75\includes\nusoap\lib\class.soap_server.php
* oldClassConstructors
 * Line 160: `	function soap_server($wsdl=false){`

#### C:\Users\marti\Documents\gambio_tickets75\includes\nusoap\lib\class.soap_transport_http.php
* oldClassConstructors
 * Line 43: `	function soap_transport_http($url){`
* deprecatedFunctions
 * Line 377: `			set_magic_quotes_runtime(0);`

#### C:\Users\marti\Documents\gambio_tickets75\includes\nusoap\lib\class.soap_val.php
* oldClassConstructors
 * Line 67: `  	function soapval($name='soapval',$type=false,$value=-1,$element_ns=false,$type_ns=false,$attributes=false) {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\nusoap\lib\class.soapclientw.php
* oldClassConstructors
 * Line 86: `	function soapclientw($endpoint,$wsdl = false,$proxyhost = false,$proxyport = false,$proxyusername = false, $proxypassword = false, $timeout = 0, $response_timeout = 30){`
* newOperatorWithReference
 * Line 107: `				$this->wsdl =& new wsdl($this->wsdlFile,$this->proxyhost,$this->proxyport,$this->proxyusername,$this->proxypassword,$this->timeout,$this->response_timeout);`

#### C:\Users\marti\Documents\gambio_tickets75\includes\nusoap\lib\class.wsdl.php
* oldClassConstructors
 * Line 56: `    function wsdl($wsdl = '',$proxyhost=false,$proxyport=false,$proxyusername=false,$proxypassword=false,$timeout=0,$response_timeout=30){`

#### C:\Users\marti\Documents\gambio_tickets75\includes\nusoap\lib\class.wsdlcache.php
* oldClassConstructors
 * Line 38: `	function wsdlcache($cache_dir='.', $cache_lifetime=0) {`

#### C:\Users\marti\Documents\gambio_tickets75\includes\nusoap\lib\class.xmlschema.php
* oldClassConstructors
 * Line 52: `	function XMLSchema($schema='',$xml='',$namespaces=array()){`

#### C:\Users\marti\Documents\gambio_tickets75\includes\nusoap\lib\nusoap.php
* oldClassConstructors
 * Line 182: `	function nusoap_base() {`
 * Line 889: `	function soap_fault($faultcode,$faultactor='',$faultstring='',$faultdetail=''){`
 * Line 973: `	function XMLSchema($schema='',$xml='',$namespaces=array()){`
 * Line 1863: `  	function soapval($name='soapval',$type=false,$value=-1,$element_ns=false,$type_ns=false,$attributes=false) {`
 * Line 1934: `	function soap_transport_http($url){`
 * Line 3043: `	function soap_server($wsdl=false){`
 * Line 3935: `    function wsdl($wsdl = '',$proxyhost=false,$proxyport=false,$proxyusername=false,$proxypassword=false,$timeout=0,$response_timeout=30){`
 * Line 5626: `	function soap_parser($xml,$encoding='UTF-8',$method='',$decode_utf8=true){`
 * Line 6234: `	function soapclientw($endpoint,$wsdl = false,$proxyhost = false,$proxyport = false,$proxyusername = false, $proxypassword = false, $timeout = 0, $response_timeout = 30){`
* deprecatedFunctions
 * Line 2268: `			set_magic_quotes_runtime(0);`
* newOperatorWithReference
 * Line 6255: `				$this->wsdl =& new wsdl($this->wsdlFile,$this->proxyhost,$this->proxyport,$this->proxyusername,$this->proxypassword,$this->timeout,$this->response_timeout);`

#### C:\Users\marti\Documents\gambio_tickets75\includes\nusoap\lib\nusoapmime.php
* newOperatorWithReference
 * Line 114: `			$mimeMessage =& new Mail_mimePart('', $params);`
 * Line 321: `			$mimeMessage =& new Mail_mimePart('', $params);`

#### C:\Users\marti\Documents\gambio_tickets75\includes\nusoap\luup_webpayments.php
* oldClassConstructors
 * Line 33: `	function luup_webpayments( $soapPath, $luupwsdl = '' ) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\Common\ClassLoader.php
* variableInterpolation
 * Line 225: `                } else if ($loader[0]::$loader[1]($className)) { // array('ClassName', 'methodName')`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\DBAL\Types\Type.php
* variableInterpolation
 * Line 160: `            self::$_typeObjects[$name] = new self::$_typesMap[$name]();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Amf\Parse\Resource\MysqlResult.php
* deprecatedFunctions
 * Line 52: `        $fieldcnt = mysql_num_fields($resource);`
 * Line 55: `            $type = mysql_field_type($resource, $i);`
 * Line 57: `                $fields_transform[mysql_field_name($resource, $i)] = self::$fieldTypes[$type];`
 * Line 60: `        while($row = mysql_fetch_object($resource)) {`

#### C:\Users\marti\Documents\gambio_tickets75\login_admin.php
* deprecatedFunctions
 * Line 26: `	$result = mysql_query('`
 * Line 38: `				mysql_query('`
 * Line 46: `				mysql_query('`
 * Line 51: `				mysql_query('`
 * Line 56: `				mysql_query('`
 * Line 64: `				mysql_query('`
 * Line 72: `				mysql_query('`
 * Line 77: `				mysql_query('`
 * Line 82: `				mysql_query('`
 * Line 87: `				mysql_query('`
 * Line 92: `				mysql_query('`
 * Line 100: `				mysql_query('`
 * Line 108: `				mysql_query('`

#### C:\Users\marti\Documents\gambio_tickets75\masterpayment_response.php
* oldClassConstructors
 * Line 30: `	function MasterpaymentResponse($_var)`

#### C:\Users\marti\Documents\gambio_tickets75\paypal_checkout.php
* deprecatedFunctions
 * Line 110: `					if(mysql_num_rows($gm_attribute_stock) == 1) $gm_stock_error = true;`
* variableInterpolation
 * Line 442: `if (isset ($$_SESSION['payment']->form_action_url) && !$$_SESSION['payment']->tmpOrders) {`
 * Line 443: `	$form_action_url = $$_SESSION['payment']->form_action_url;`

#### C:\Users\marti\Documents\gambio_tickets75\popup_coupon_help.php
* deprecatedFunctions
 * Line 112: `mysql_close();`

#### C:\Users\marti\Documents\gambio_tickets75\popup_cvv.php
* deprecatedFunctions
 * Line 72: `mysql_close(); `

#### C:\Users\marti\Documents\gambio_tickets75\popup_image.php
* deprecatedFunctions
 * Line 101: `mysql_close(); `

#### C:\Users\marti\Documents\gambio_tickets75\popup_search_help.php
* deprecatedFunctions
 * Line 35: `mysql_close(); `

#### C:\Users\marti\Documents\gambio_tickets75\print_order.php
* deprecatedFunctions
 * Line 66: `mysql_close();`

#### C:\Users\marti\Documents\gambio_tickets75\print_product_info.php
* deprecatedFunctions
 * Line 113: `mysql_close();`

#### C:\Users\marti\Documents\gambio_tickets75\request_port.php
* deprecatedFunctions
 * Line 123: `mysql_close();`

#### C:\Users\marti\Documents\gambio_tickets75\scripts\sendmail_observer_eventim_de.php
* deprecatedFunctions
 * Line 13: `	$link = mysql_connect('localhost', 'observer', 'Z3aQaWBcXS1v');`
 * Line 15: `	    die('Keine Verbindung möglich: ' . mysql_error());`
 * Line 17: `	mysql_select_db('ticketobserver');`
 * Line 18: `	$result = mysql_query("SELECT * FROM observed_eventim WHERE hash = '".$cookiename."'");`
 * Line 20: `	    echo 'Konnte Abfrage nicht ausführen: ' . mysql_error();`
 * Line 23: `	$row = mysql_fetch_array($result);`
 * Line 52: `			mysql_query("INSERT INTO observed_eventim (hash, timecode) VALUES ('".$cookiename."', ".strtotime($dateFuture).")");`
 * Line 54: `			mysql_query("UPDATE observed_eventim SET timecode='".strtotime($dateFuture)."' WHERE hash='".$cookiename."'");`

#### C:\Users\marti\Documents\gambio_tickets75\scripts\sendmail_observer_eventim_de2.php
* deprecatedFunctions
 * Line 13: `	$link = mysql_connect('localhost', 'observer', 'Z3aQaWBcXS1v');`
 * Line 15: `	    die('Keine Verbindung möglich: ' . mysql_error());`
 * Line 17: `	mysql_select_db('ticketobserver');`
 * Line 18: `	$result = mysql_query("SELECT * FROM observed_eventim WHERE hash = '".$cookiename."'");`
 * Line 20: `	    echo 'Konnte Abfrage nicht ausführen: ' . mysql_error();`
 * Line 23: `	$row = mysql_fetch_array($result);`
 * Line 52: `			mysql_query("INSERT INTO observed_eventim (hash, timecode) VALUES ('".$cookiename."', ".strtotime($dateFuture).")");`
 * Line 54: `			mysql_query("UPDATE observed_eventim SET timecode='".strtotime($dateFuture)."' WHERE hash='".$cookiename."'");`

#### C:\Users\marti\Documents\gambio_tickets75\scripts\sendmail_observer_tickets_de.php
* deprecatedFunctions
 * Line 7: `	$link = mysql_connect('localhost', 'observer', 'Z3aQaWBcXS1v');`
 * Line 9: `	    die('Keine Verbindung möglich: ' . mysql_error());`
 * Line 11: `	mysql_select_db('ticketobserver');`
 * Line 12: `	$result = mysql_query("SELECT * FROM observed_tickets WHERE hash = '".$cookiename."'");`
 * Line 14: `	    echo 'Konnte Abfrage nicht ausführen: ' . mysql_error();`
 * Line 17: `	$row = mysql_fetch_array($result);`
 * Line 46: `			mysql_query("INSERT INTO observed_tickets (id, hash, timecode) VALUES ('".$_GET["id"]."', '".$cookiename."', ".strtotime($dateFuture).")");`
 * Line 48: `			mysql_query("UPDATE observed_tickets SET timecode='".strtotime($dateFuture)."' WHERE hash='".$cookiename."'");`

#### C:\Users\marti\Documents\gambio_tickets75\scripts\sendmail_observer_tickets_de2.php
* deprecatedFunctions
 * Line 6: `	$link = mysql_connect('localhost', 'observer', 'Z3aQaWBcXS1v');`
 * Line 8: `	    die('Keine Verbindung möglich: ' . mysql_error());`
 * Line 10: `	mysql_select_db('ticketobserver');`
 * Line 11: `	$result = mysql_query("SELECT * FROM observed WHERE hash = '".$cookiename."'");`
 * Line 13: `	    echo 'Konnte Abfrage nicht ausführen: ' . mysql_error();`
 * Line 16: `	$row = mysql_fetch_array($result);`
 * Line 45: `			mysql_query("INSERT INTO observed (id, hash, timecode) VALUES ('".$_GET["id"]."', '".$cookiename."', ".strtotime($dateFuture).")");`
 * Line 47: `			mysql_query("UPDATE observed SET timecode='".strtotime($dateFuture)."' WHERE hash='".$cookiename."'");`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\CacheControl.inc.php
* oldClassConstructors
 * Line 22: `    function CacheControl() {`
* deprecatedFunctions
 * Line 85: `        while (($t_row = mysql_fetch_array($t_result))) {`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\CategoriesAgent.inc.php
* oldClassConstructors
 * Line 25: `	function CategoriesAgent()`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\FeatureFilter\CategoriesFilter.inc.php
* oldClassConstructors
 * Line 25: `  function CategoriesFilter()`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\FeatureFilter\Feature.inc.php
* oldClassConstructors
 * Line 22: `  function Feature()`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\FeatureFilter\FeatureControl.inc.php
* oldClassConstructors
 * Line 16: `  function FeatureControl()`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\FeatureFilter\FeatureValue.inc.php
* oldClassConstructors
 * Line 24: `  function FeatureValue()`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\FeatureFilter\FilterControl.inc.php
* oldClassConstructors
 * Line 16: `  function FilterControl()`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\FeatureFilter\FilterManager.inc.php
* oldClassConstructors
 * Line 22: `	function FilterManager()`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\FeatureFilter\IndexFeatureProductFinder.inc.php
* oldClassConstructors
 * Line 24: `	function IndexFeatureProductFinder()`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\FeatureFilter\ProductFeatureHandler.inc.php
* oldClassConstructors
 * Line 16: `	function ProductFeatureHandler( )`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\LanguageTextManager.inc.php
* oldClassConstructors
 * Line 46: `	function LanguageTextManager($p_default_section, $p_default_language_id)`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\ListingManager.inc.php
* oldClassConstructors
 * Line 13: `	function ListingManager()`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\PageTrack.inc.php
* oldClassConstructors
 * Line 20: `  function PageTrack()`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\QuantityUnit\ProductQuantityUnitHandler.inc.php
* oldClassConstructors
 * Line 16: `	function ProductQuantityUnitHandler()`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\QuantityUnit\QuantityUnit.inc.php
* oldClassConstructors
 * Line 21: `	function QuantityUnit()`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\QuantityUnit\QuantityUnitControl.inc.php
* oldClassConstructors
 * Line 16: `	function QuantityUnitControl()`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\ShopURLHandler.inc.php
* oldClassConstructors
 * Line 23: `	function ShopURLHandler()`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\SliderSet\CategorySliderHandler.inc.php
* oldClassConstructors
 * Line 16: `	function CategorySliderHandler()`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\SliderSet\SliderControl.inc.php
* oldClassConstructors
 * Line 16: `	function SliderControl( )`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\SliderSet\SliderSet.inc.php
* oldClassConstructors
 * Line 24: `  function SliderSet()`

#### C:\Users\marti\Documents\gambio_tickets75\system\controls\TemplateControl.inc.php
* oldClassConstructors
 * Line 47: `	function TemplateControl($p_template_name)`

#### C:\Users\marti\Documents\gambio_tickets75\system\core\ClassRegistry.inc.php
* oldClassConstructors
 * Line 20: `  function ClassRegistry()`

#### C:\Users\marti\Documents\gambio_tickets75\system\core\DataCache.inc.php
* oldClassConstructors
 * Line 18: `	function DataCache()`

#### C:\Users\marti\Documents\gambio_tickets75\system\core\Debugger.inc.php
* oldClassConstructors
 * Line 17: `	function Debugger()`

#### C:\Users\marti\Documents\gambio_tickets75\system\core\MainFactory.inc.php
* oldClassConstructors
 * Line 21: `	function MainFactory()`

#### C:\Users\marti\Documents\gambio_tickets75\system\core\Registry.inc.php
* oldClassConstructors
 * Line 20: `  function Registry()`

#### C:\Users\marti\Documents\gambio_tickets75\system\core\StopWatch.inc.php
* oldClassConstructors
 * Line 35: `    function StopWatch($p_warning_time_limit = 0.01)`

#### C:\Users\marti\Documents\gambio_tickets75\system\data\GMDataObject.inc.php
* oldClassConstructors
 * Line 23: `	function GMDataObject($p_db_table, $p_key_values_array=false, $p_orderby_keys_array=false)`

#### C:\Users\marti\Documents\gambio_tickets75\system\data\GMDataObjectGroup.inc.php
* oldClassConstructors
 * Line 18: `	function GMDataObjectGroup($p_db_table, $p_key_values_array=false, $p_orderby_keys_array=false)`

#### C:\Users\marti\Documents\gambio_tickets75\system\data\SimpleBoxesMaster.inc.php
* oldClassConstructors
 * Line 18: `	function SimpleBoxesMaster()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\AdvancedSearchContentView.inc.php
* oldClassConstructors
 * Line 23: `	function AdvancedSearchContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\ContentView.inc.php
* oldClassConstructors
 * Line 28: `	function ContentView($p_get_array=false, $p_post_array=false) `

#### C:\Users\marti\Documents\gambio_tickets75\system\views\FooterContentView.inc.php
* oldClassConstructors
 * Line 22: `	function FooterContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\LoginContentView.inc.php
* oldClassConstructors
 * Line 26: `	function LoginContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\LogoffContentView.inc.php
* oldClassConstructors
 * Line 28: `	function LogoffContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\MegaFlyoverContentView.inc.php
* oldClassConstructors
 * Line 30: `	function MegaFlyoverContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\NewsletterContentView.inc.php
* oldClassConstructors
 * Line 23: `	function NewsletterContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\ProductReviewsInfoContentView.inc.php
* oldClassConstructors
 * Line 22: `	function ProductReviewsInfoContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\account\AccountContentView.inc.php
* oldClassConstructors
 * Line 27: `	function AccountContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\account\AddressBookContentView.inc.php
* oldClassConstructors
 * Line 23: `	function AddressBookContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\account\AddressBookProcessContentView.inc.php
* oldClassConstructors
 * Line 19: `	function AddressBookProcessContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\product_info\AlsoPurchasedContentView.inc.php
* oldClassConstructors
 * Line 19: `	function AlsoPurchasedContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\product_info\CrossSellingContentView.inc.php
* oldClassConstructors
 * Line 22: `	function CrossSellingContentView($p_type = 'cross_selling')`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\product_info\GraduatedPricesContentView.inc.php
* oldClassConstructors
 * Line 19: `	function GraduatedPricesContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\product_info\LightboxEventContentView.inc.php
* oldClassConstructors
 * Line 14: `	function LightboxEventContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\product_info\LightboxGalleryContentView.inc.php
* oldClassConstructors
 * Line 15: `	function LightboxGalleryContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\product_info\PriceOfferContentView.inc.php
* oldClassConstructors
 * Line 20: `	function PriceOfferContentView()`
* deprecatedFunctions
 * Line 72: `						$get_attributes = mysql_query("SELECT `

#### C:\Users\marti\Documents\gambio_tickets75\system\views\product_info\ProductAttributesContentView.inc.php
* oldClassConstructors
 * Line 27: `	function ProductAttributesContentView($p_template = 'default')`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\product_info\ProductInfoContentView.inc.php
* oldClassConstructors
 * Line 41: `	function ProductInfoContentView($p_template = 'default')`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\product_info\ProductMediaContentView.inc.php
* oldClassConstructors
 * Line 19: `	function ProductMediaContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\product_info\ProductNavigatorContentView.inc.php
* oldClassConstructors
 * Line 15: `	function ProductNavigatorContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\product_info\ProductReviewsContentView.inc.php
* oldClassConstructors
 * Line 22: `	function ProductReviewsContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\product_info\TellAFriendContentView.inc.php
* oldClassConstructors
 * Line 17: `	function TellAFriendContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\shopping_cart\GiftCartContentView.inc.php
* oldClassConstructors
 * Line 23: `	function GiftCartContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\shopping_cart\OrderDetailsCartContentView.inc.php
* oldClassConstructors
 * Line 41: `	function OrderDetailsCartContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\shopping_cart\ShoppingCartContentView.inc.php
* oldClassConstructors
 * Line 27: `	function ShoppingCartContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\wish_list\OrderDetailsWishListContentView.inc.php
* oldClassConstructors
 * Line 36: `	function OrderDetailsWishListContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\system\views\wish_list\WishListContentView.inc.php
* oldClassConstructors
 * Line 27: `	function WishListContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\gm_dynamic.css.php
* deprecatedFunctions
 * Line 65: `			$conn_id = mysql_pconnect(`
 * Line 73: `			$conn_id = mysql_connect(`
 * Line 79: `		mysql_select_db(DB_DATABASE, $conn_id);`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\AddAQuickieContentView.inc.php
* oldClassConstructors
 * Line 22: `	function AddAQuickieContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\AdminContentView.inc.php
* oldClassConstructors
 * Line 21: `	function AdminContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\BestsellersContentView.inc.php
* oldClassConstructors
 * Line 25: `	function BestsellersContentView() `

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\BookmarksContentView.inc.php
* oldClassConstructors
 * Line 20: `	function BookmarksContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\CategoriesContentView.inc.php
* oldClassConstructors
 * Line 14: `	function CategoriesContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\CategoriesSubmenusContentView.inc.php
* oldClassConstructors
 * Line 13: `	function CategoriesSubmenusContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\ContentContentView.inc.php
* oldClassConstructors
 * Line 19: `	function ContentContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\CounterContentView.inc.php
* oldClassConstructors
 * Line 20: `	function CounterContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\CurrenciesContentView.inc.php
* oldClassConstructors
 * Line 21: `	function CurrenciesContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\EbayContentView.inc.php
* oldClassConstructors
 * Line 19: `	function EbayContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\ExtraboxesContentView.inc.php
* oldClassConstructors
 * Line 19: `	function ExtraboxesContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\FilterContentView.inc.php
* oldClassConstructors
 * Line 17: `	function FilterContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\ImageSliderContentView.inc.php
* oldClassConstructors
 * Line 16: `	function ImageSliderContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\InfoboxContentView.inc.php
* oldClassConstructors
 * Line 23: `	function InfoboxContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\InformationContentView.inc.php
* oldClassConstructors
 * Line 19: `	function InformationContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\InformationContentView2.inc.php
* oldClassConstructors
 * Line 19: `	function InformationContentView2()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\InformationContentView3.inc .php
* oldClassConstructors
 * Line 19: `	function InformationContentView3()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\InformationContentView4.inc .php
* oldClassConstructors
 * Line 19: `	function InformationContentView4()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\InformationContentView5.inc.php
* oldClassConstructors
 * Line 19: `	function InformationContentView5()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\LanguagesContentView.inc.php
* oldClassConstructors
 * Line 19: `	function LanguagesContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\LastViewedContentView.inc.php
* oldClassConstructors
 * Line 19: `	function LastViewedContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\LoginboxContentView.inc.php
* oldClassConstructors
 * Line 23: `	function LoginboxContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\ManufacturersContentView.inc.php
* oldClassConstructors
 * Line 23: `	function ManufacturersContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\ManufacturersInfoContentView.inc.php
* oldClassConstructors
 * Line 19: `	function ManufacturersInfoContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\NewsletterContentView.inc.php
* oldClassConstructors
 * Line 25: `	function NewsletterContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\OrderHistoryContentView.inc.php
* oldClassConstructors
 * Line 21: `	function OrderHistoryContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\PayPalContentView.inc.php
* oldClassConstructors
 * Line 19: `	function PayPalContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\ReviewsContentView.inc.php
* oldClassConstructors
 * Line 22: `	function ReviewsContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\ScrollerContentView.inc.php
* oldClassConstructors
 * Line 21: `	function ScrollerContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\SearchContentView.inc.php
* oldClassConstructors
 * Line 21: `	function SearchContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\ShoppingCartDropdown.inc.php
* oldClassConstructors
 * Line 23: `	function ShoppingCartDropdown()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\SpecialsContentView.inc.php
* oldClassConstructors
 * Line 21: `	function SpecialsContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\TopNavigationContentView.inc.php
* oldClassConstructors
 * Line 14: `	function TopNavigationContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\TrustedContentView.inc.php
* oldClassConstructors
 * Line 22: `	function TrustedContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\TrustedWidgetContentView.inc.php
* oldClassConstructors
 * Line 19: `	function TrustedWidgetContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\WhatsNewContentView.inc.php
* oldClassConstructors
 * Line 26: `	function WhatsNewContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\YoochooseAlsoClicked.inc.php
* oldClassConstructors
 * Line 22: `	function YoochooseAlsoClicked() {`

#### C:\Users\marti\Documents\gambio_tickets75\templates\EyeCandy\source\classes\YoochooseTopSelling.inc.php
* oldClassConstructors
 * Line 22: `	function YoochooseTopSelling() {`

#### C:\Users\marti\Documents\gambio_tickets75\templates\gambio\gm_dynamic.css.php
* deprecatedFunctions
 * Line 62: `			$conn_id = mysql_pconnect(`
 * Line 70: `			$conn_id = mysql_connect(`
 * Line 77: `		mysql_select_db(DB_DATABASE, $conn_id);`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\AddAQuickieContentView.inc.php
* oldClassConstructors
 * Line 22: `	function AddAQuickieContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\AdminContentView.inc.php
* oldClassConstructors
 * Line 21: `	function AdminContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\AdvancedSearchContentView.inc.php
* oldClassConstructors
 * Line 23: `	function AdvancedSearchContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\BestsellersContentView.inc.php
* oldClassConstructors
 * Line 25: `	function BestsellersContentView() `

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\BookmarksContentView.inc.php
* oldClassConstructors
 * Line 20: `	function BookmarksContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\CategoriesContentView.inc.php
* oldClassConstructors
 * Line 15: `	function CategoriesContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\CategoriesSubmenusContentView.inc.php
* oldClassConstructors
 * Line 13: `	function CategoriesSubmenusContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\ChooseLanguageMobileContentView.inc.php
* oldClassConstructors
 * Line 19: `	function ChooseLanguageMobileContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\ContactContentView.inc.php
* oldClassConstructors
 * Line 24: `	function ContactContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\ContentContentView.inc.php
* oldClassConstructors
 * Line 19: `	function ContentContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\CounterContentView.inc.php
* oldClassConstructors
 * Line 20: `	function CounterContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\CurrenciesContentView.inc.php
* oldClassConstructors
 * Line 21: `	function CurrenciesContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\EbayContentView.inc.php
* oldClassConstructors
 * Line 19: `	function EbayContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\ExtraboxesContentView.inc.php
* oldClassConstructors
 * Line 19: `	function ExtraboxesContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\FilterContentView.inc.php
* oldClassConstructors
 * Line 17: `	function FilterContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\FooterCustomerReviewsContentView.inc.php
* oldClassConstructors
 * Line 21: `	function FooterCustomerReviewsContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\ImageSliderContentView.inc.php
* oldClassConstructors
 * Line 16: `	function ImageSliderContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\LanguagesContentView.inc.php
* oldClassConstructors
 * Line 19: `    function LanguagesContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\LastViewedContentView.inc.php
* oldClassConstructors
 * Line 19: `	function LastViewedContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\LoginboxContentView.inc.php
* oldClassConstructors
 * Line 23: `	function LoginboxContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\ManufacturersContentView.inc.php
* oldClassConstructors
 * Line 23: `	function ManufacturersContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\ManufacturersInfoContentView.inc.php
* oldClassConstructors
 * Line 19: `	function ManufacturersInfoContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\NewsletterContentView.inc.php
* oldClassConstructors
 * Line 25: `	function NewsletterContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\OrderDetailsCartContentView.inc.php
* oldClassConstructors
 * Line 43: `	function OrderDetailsCartContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\OrderHistoryContentView.inc.php
* oldClassConstructors
 * Line 21: `	function OrderHistoryContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\PayPalContentView.inc.php
* oldClassConstructors
 * Line 19: `	function PayPalContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\PhotoCreditsContentView.inc.php
* oldClassConstructors
 * Line 24: `	function PhotoCreditsContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\ProductAttributesContentView.inc.php
* oldClassConstructors
 * Line 29: `	function ProductAttributesContentView($p_template = 'default')`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\ProductInfoCollapsiblesContentView.inc.php
* oldClassConstructors
 * Line 7: `	function ProductInfoCollapsiblesContentView()`
* deprecatedFunctions
 * Line 33: `	        WHERE PD.products_name = '" . mysql_real_escape_string($p_coo_product->data['products_name']) . "'`
 * Line 34: `	        AND P.products_id != " . mysql_real_escape_string($p_coo_product->data['products_id']) . "`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\ProductInfoContentView.inc.php
* oldClassConstructors
 * Line 45: `    function ProductInfoContentView($p_template = 'default')`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\ProductListingRecentViewedProductsContentView.inc.php
* oldClassConstructors
 * Line 4: `	function ProductListingRecentViewedProductsContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\RecentlyViewedProductsContentView.inc.php
* oldClassConstructors
 * Line 25: `	function RecentlyViewedProductsContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\ReviewsContentView.inc.php
* oldClassConstructors
 * Line 22: `	function ReviewsContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\ScrollerContentView.inc.php
* oldClassConstructors
 * Line 21: `	function ScrollerContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\SearchContentView.inc.php
* oldClassConstructors
 * Line 21: `	function SearchContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\ShoppingCartContentView.inc.php
* oldClassConstructors
 * Line 28: `	function ShoppingCartContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\ShoppingCartDropdown.inc.php
* oldClassConstructors
 * Line 23: `    function ShoppingCartDropdown()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\SpecialsContentView.inc.php
* oldClassConstructors
 * Line 21: `	function SpecialsContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\TicketalarmContentView.inc.php
* oldClassConstructors
 * Line 5: `    function TicketalarmContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\TopNavigationContentView.inc.php
* oldClassConstructors
 * Line 14: `	function TopNavigationContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\TrustedContentView.inc.php
* oldClassConstructors
 * Line 22: `	function TrustedContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\TrustedWidgetContentView.inc.php
* oldClassConstructors
 * Line 19: `	function TrustedWidgetContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\WhatsNewContentView.inc.php
* oldClassConstructors
 * Line 26: `	function WhatsNewContentView()`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\YoochooseAlsoClicked.inc.php
* oldClassConstructors
 * Line 22: `	function YoochooseAlsoClicked() {`

#### C:\Users\marti\Documents\gambio_tickets75\templates\tickets75\source\classes\YoochooseTopSelling.inc.php
* oldClassConstructors
 * Line 22: `	function YoochooseTopSelling() {`

#### C:\Users\marti\Documents\gambio_tickets75\vrepay_kreditkarte.php
* oldClassConstructors
 * Line 17: `	function vrepay_kreditkarte() {`

#### C:\Users\marti\Documents\gambio_tickets75\xtbcallback.php
* deprecatedFunctions
 * Line 161: `			$rs = xtc_db_query($QUERY); $SQLACTION_RESULT = mysql_affected_rows()." rows affected";			`


# syntax
#### C:\Users\marti\Documents\gambio_tickets75\admin\gm\classes\GMProductExport.php
* syntax
 * Line 368: `    $t_modules = array(); //Fatal error: 'break' not in the 'loop' or 'switch' context on line 368`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\afterbuy_parse_beschreibung_neu.03.2016.php
* syntax
 * Line 1643: `		$prefix_weight = "+"; //Fatal error: Redefinition of parameter $ab_quantity on line 1643`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\afterbuy_parse_beschreibung_neu.06.2015.php
* syntax
 * Line 1640: `		$prefix_weight = "+"; //Fatal error: Redefinition of parameter $ab_quantity on line 1640`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\classes\sessions.php
* syntax
 * Line 38: `    var $id; //Fatal error: Constant expression contains invalid operations on line 38`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\javascript\elFinder\php\libs\GdBmp.php
* syntax
 * Line 70: `class elFinderLibGdBmp{ //Fatal error: Cannot redeclare imagecreatefrombmp() on line 70`

#### C:\Users\marti\Documents\gambio_tickets75\admin\products_attributes_old.php
* syntax
 * Line 1274: `											}  //Parse error: syntax error, unexpected 'elseif' (T_ELSEIF), expecting end of file on line 1274`

#### C:\Users\marti\Documents\gambio_tickets75\checkout_success_old.php
* syntax
 * Line 104: `		<noscript> //Parse error: syntax error, unexpected '*', expecting end of file on line 104`

#### C:\Users\marti\Documents\gambio_tickets75\export\cao_update.php
* syntax
 * Line 141: `                      'tmp_name' => $HTTP_POST_FILES[$this->file]['tmp_name']); //Fatal error: Cannot re-assign $this on line 141`

#### C:\Users\marti\Documents\gambio_tickets75\ext\clickandbuy\lib\nusoap.php
* syntax
 * Line 6478: `	* @param	integer $response_timeout set response timeout in seconds //Parse error: syntax error, unexpected 'new' (T_NEW) on line 6478`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\IclearCore.php
* syntax
 * Line 269: `       //Parse error: syntax error, unexpected 'new' (T_NEW) on line 269`

#### C:\Users\marti\Documents\gambio_tickets75\iclear\lib\nusoap.php
* syntax
 * Line 6513: `			$this->xml_encoding = 'ISO-8859-1'; //Parse error: syntax error, unexpected 'new' (T_NEW) on line 6513`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\banktransfer_validation.php
* syntax
 * Line 1209: `    $AccountNo = $this->ExpandAccount($AccountNo); //Parse error: Invalid numeric literal on line 1209`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\sessions.php
* syntax
 * Line 244: `  } //Fatal error: Cannot redeclare session_name() on line 244`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\xtcPrice.php
* syntax
 * Line 341: `    function xtcFormat($price, $format, $tax_class = 0, $curr = false, $vpeStatus = 0, $pID = 0) { //Fatal error: Redefinition of parameter $vpeStatus on line 341`

#### C:\Users\marti\Documents\gambio_tickets75\includes\nusoap\lib\class.soapclientw.php
* syntax
 * Line 114: `				$this->setError('wsdl error: '.$errstr); //Parse error: syntax error, unexpected 'new' (T_NEW) on line 114`

#### C:\Users\marti\Documents\gambio_tickets75\includes\nusoap\lib\nusoap.php
* syntax
 * Line 6496: `		$this->checkCookies(); //Parse error: syntax error, unexpected 'new' (T_NEW) on line 6496`

#### C:\Users\marti\Documents\gambio_tickets75\includes\nusoap\lib\nusoapmime.php
* syntax
 * Line 130: `						$data = fread($fd, filesize($att['filename'])); //Parse error: syntax error, unexpected 'new' (T_NEW) on line 130`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\Common\Cache\RiakCache.php
* syntax
 * Line 26: ` * Riak cache provider. //Fatal error: Cannot use Riak\Object as Object because 'Object' is a special class name on line 26`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Service\WindowsAzure\Storage\Batch.php
* syntax
 * Line 108: `	/** //Fatal error: Cannot unset $this on line 108`

#### C:\Users\marti\Documents\gambio_tickets75\mapa_redirect.php
* syntax
 * Line 53: `</center> //Parse error: syntax error, unexpected 'else' (T_ELSE) on line 53`


# nuance
#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\classes\pclzip.lib.php
* funcGetArg
 * Line 258: `      $v_arg_list = func_get_args();`
 * Line 438: `      $v_arg_list = func_get_args();`
 * Line 687: `      $v_arg_list = func_get_args();`
 * Line 830: `      $v_arg_list = func_get_args();`
 * Line 961: `      $v_arg_list = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\javascript\elFinder\php\elFinder.class.php
* funcGetArg
 * Line 989: `		foreach (func_get_args() as $msg) {`

#### C:\Users\marti\Documents\gambio_tickets75\admin\includes\javascript\elFinder\php\elFinderVolumeDriver.class.php
* funcGetArg
 * Line 2827: `		foreach (func_get_args() as $err) {`
 * Line 2835: `		// $this->error = is_array($error) ? $error : func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\Smarty_2.6.14\Smarty.class.php
* funcGetArg
 * Line 1526: `        $_args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\less.php\Less.php
* funcGetArg
 * Line 2824: `		$string = func_get_arg(0);`
 * Line 2825: `		$args = func_get_args();`
 * Line 2891: `		$args = func_get_args();`
 * Line 2979: `		$args = func_get_args();`
 * Line 2983: `		$args = func_get_args();`
 * Line 3131: `		$arguments = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\includes\classes\secupay_api.php
* funcGetArg
 * Line 127: `			foreach(func_get_args() as $val){`
 * Line 148: `		foreach(func_get_args() as $val){`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\Common\Collections\ExpressionBuilder.php
* funcGetArg
 * Line 42: `        return new CompositeExpression(CompositeExpression::TYPE_AND, func_get_args());`
 * Line 51: `        return new CompositeExpression(CompositeExpression::TYPE_OR, func_get_args());`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\Common\Proxy\ProxyGenerator.php
* foreachByReference
 * Line 521: `        foreach ($allProperties as &$property) {`
 * Line 524: `        foreach ($protectedProperties as &$property) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\DBAL\Connection.php
* funcGetArg
 * Line 686: `        $args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\DBAL\Connections\MasterSlaveConnection.php
* funcGetArg
 * Line 307: `        $args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\DBAL\Driver\IBMDB2\DB2Connection.php
* funcGetArg
 * Line 62: `        $args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\DBAL\Driver\Mysqli\MysqliConnection.php
* funcGetArg
 * Line 74: `        $args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\DBAL\Driver\Mysqli\MysqliStatement.php
* arrayValueByReference
 * Line 162: `                    $refs[$key] =& $value;`
* foreachByReference
 * Line 185: `        foreach ($values as &$v) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\DBAL\Driver\OCI8\OCI8Connection.php
* funcGetArg
 * Line 72: `        $args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\DBAL\Driver\SQLSrv\SQLSrvConnection.php
* funcGetArg
 * Line 65: `        $args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\DBAL\Driver\SQLSrv\SQLSrvStatement.php
* funcGetArg
 * Line 202: `                $args = func_get_args();`
 * Line 218: `            $args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\DBAL\Platforms\AbstractPlatform.php
* funcGetArg
 * Line 695: `        return join(' || ' , func_get_args());`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\DBAL\Platforms\DrizzlePlatform.php
* funcGetArg
 * Line 50: `        $args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\DBAL\Platforms\MySqlPlatform.php
* funcGetArg
 * Line 94: `        $args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\DBAL\Platforms\SQLServerPlatform.php
* foreachByReference
 * Line 176: `        foreach ($columns as &$column) {`
 * Line 715: `        foreach ($orderByParts as &$part) {`
* funcGetArg
 * Line 574: `        $args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\DBAL\Portability\Connection.php
* funcGetArg
 * Line 123: `        $stmt = call_user_func_array(array($this->_conn, 'query'), func_get_args());`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\DBAL\Query\Expression\ExpressionBuilder.php
* funcGetArg
 * Line 68: `        return new CompositeExpression(CompositeExpression::TYPE_AND, func_get_args());`
 * Line 86: `        return new CompositeExpression(CompositeExpression::TYPE_OR, func_get_args());`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\DBAL\Query\QueryBuilder.php
* funcGetArg
 * Line 397: `        $selects = is_array($select) ? $select : func_get_args();`
 * Line 421: `        $selects = is_array($select) ? $select : func_get_args();`
 * Line 653: `            $predicates = new CompositeExpression(CompositeExpression::TYPE_AND, func_get_args());`
 * Line 678: `        $args = func_get_args();`
 * Line 708: `        $args = func_get_args();`
 * Line 737: `        $groupBy = is_array($groupBy) ? $groupBy : func_get_args();`
 * Line 760: `        $groupBy = is_array($groupBy) ? $groupBy : func_get_args();`
 * Line 774: `            $having = new CompositeExpression(CompositeExpression::TYPE_AND, func_get_args());`
 * Line 789: `        $args = func_get_args();`
 * Line 809: `        $args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\DBAL\Schema\AbstractSchemaManager.php
* funcGetArg
 * Line 85: `        $args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\DBAL\Schema\SQLServerSchemaManager.php
* foreachByReference
 * Line 129: `        foreach ($tableIndexRows as &$tableIndex) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\ORM\Query\Expr.php
* funcGetArg
 * Line 50: `        return new Expr\Andx(func_get_args());`
 * Line 68: `        return new Expr\Orx(func_get_args());`
 * Line 254: `        return 'COUNT(DISTINCT ' . implode(', ', func_get_args()) . ')';`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\ORM\QueryBuilder.php
* funcGetArg
 * Line 521: `        $selects = is_array($select) ? $select : func_get_args();`
 * Line 564: `        $selects = is_array($select) ? $select : func_get_args();`
 * Line 770: `            $predicates = new Expr\Andx(func_get_args());`
 * Line 794: `        $args  = func_get_args();`
 * Line 824: `        $args  = func_get_args();`
 * Line 851: `        return $this->add('groupBy', new Expr\GroupBy(func_get_args()));`
 * Line 870: `        return $this->add('groupBy', new Expr\GroupBy(func_get_args()), true);`
 * Line 883: `            $having = new Expr\Andx(func_get_args());`
 * Line 897: `        $args   = func_get_args();`
 * Line 917: `        $args   = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Doctrine\ORM\Tools\Console\Command\ConvertDoctrine1SchemaCommand.php
* foreachByReference
 * Line 152: `        foreach ($fromPaths as &$dirName) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Symfony\Component\Console\Descriptor\ApplicationDescription.php
* foreachByReference
 * Line 124: `        foreach ($namespacedCommands as &$commands) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Symfony\Component\Console\Helper\FormatterHelper.php
* foreachByReference
 * Line 58: `        foreach ($messages as &$message) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Amf\Parse\Amf0\Serializer.php
* foreachByReference
 * Line 218: `        foreach ($object as $key => &$value) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Amf\Parse\Amf3\Serializer.php
* foreachByReference
 * Line 316: `        foreach ($array as $key => &$value) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Amf\Server.php
* funcGetArg
 * Line 710: `            $argv = array_slice(func_get_args(), 2);`
 * Line 741: `            $argv = array_slice(func_get_args(), 2);`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Cache\Core.php
* foreachByReference
 * Line 453: `            foreach ($ids as &$id) {`
 * Line 482: `            foreach ($ids as &$id) {`
 * Line 511: `            foreach ($ids as &$id) {`
 * Line 534: `            foreach ($ids as &$id) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Controller\Router\Route\Regex.php
* foreachByReference
 * Line 214: `            foreach ($mergedData as $key => &$value) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Db\Adapter\Abstract.php
* foreachByReference
 * Line 618: `        foreach ($where as $cond => &$term) {`
 * Line 792: `            foreach ($value as &$val) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Db\Statement\Mysqli.php
* foreachByReference
 * Line 180: `            foreach ($params as $k => &$value) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Db\Statement\Oracle.php
* foreachByReference
 * Line 387: `            foreach ($result as &$row) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Db\Table\Abstract.php
* funcGetArg
 * Line 1155: `        $args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Feed\Reader.php
* foreachByReference
 * Line 682: `        foreach ($array as &$value) {`
 * Line 686: `        foreach ($array as &$value) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Filter\Boolean.php
* funcGetArg
 * Line 85: `            $options = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Filter\Callback.php
* funcGetArg
 * Line 56: `            $options          = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Filter\File\Rename.php
* funcGetArg
 * Line 62: `            $argv = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Filter\HtmlEntities.php
* funcGetArg
 * Line 63: `            $options = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Filter\Inflector.php
* funcGetArg
 * Line 70: `            $options = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Filter\Input.php
* foreachByReference
 * Line 326: `        foreach ($data as &$element) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Filter\Null.php
* funcGetArg
 * Line 63: `            $options = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Filter\PregReplace.php
* funcGetArg
 * Line 84: `            $options = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Filter\StringToLower.php
* funcGetArg
 * Line 49: `            $options = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Filter\StringToUpper.php
* funcGetArg
 * Line 49: `            $options = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Filter\StringTrim.php
* funcGetArg
 * Line 53: `            $options          = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Filter\StripTags.php
* funcGetArg
 * Line 81: `            $options = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Form.php
* funcGetArg
 * Line 2012: `        $fromArrays = array_slice(func_get_args(),1);`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Json\Server.php
* funcGetArg
 * Line 91: `            $argv = func_get_args();`
 * Line 130: `            $argv = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Ldap\Filter\Abstract.php
* funcGetArg
 * Line 74: `        $fa = func_get_args();`
 * Line 90: `        $fa = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Ldap\Filter\Mask.php
* funcGetArg
 * Line 45: `        $args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Ldap\Filter.php
* funcGetArg
 * Line 199: `        return new Zend_Ldap_Filter_And(func_get_args());`
 * Line 213: `        return new Zend_Ldap_Filter_Or(func_get_args());`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Locale\Data.php
* foreachByReference
 * Line 100: `                foreach ($result as &$found) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Locale.php
* funcGetArg
 * Line 1145: `                $params = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Log\Formatter\Xml.php
* funcGetArg
 * Line 58: `            $args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Mail\Protocol\Imap.php
* funcGetArg
 * Line 377: `        foreach (func_get_args() as $string) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Pdf\FileParser\Font.php
* funcGetArg
 * Line 174: `            $args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Queue\Adapter\Array.php
* foreachByReference
 * Line 207: `            foreach ($temp as $key=>&$msg) {`
 * Line 249: `        foreach ($queue as $key => &$msg) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Search\Lucene\Index\SegmentInfo.php
* funcGetArg
 * Line 1531: `        $argList = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Search\Lucene\Proxy.php
* funcGetArg
 * Line 316: `        $parameters = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Search\Lucene.php
* funcGetArg
 * Line 829: `            $argList    = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Service\Delicious\PostList.php
* funcGetArg
 * Line 121: `        return $this->withTags(func_get_args());`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Service\Delicious.php
* foreachByReference
 * Line 179: `        foreach ($bundles as &$tags) {`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Session\Namespace.php
* funcGetArg
 * Line 293: `        $arg_list = func_get_args();`
 * Line 310: `        $arg_list = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Soap\Server.php
* funcGetArg
 * Line 548: `            $argv = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Stdlib\CallbackHandler.php
* funcGetArg
 * Line 209: `        return $this->call(func_get_args());`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Test\PHPUnit\Constraint\DomQuery34.php
* funcGetArg
 * Line 145: `        $argv     = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Test\PHPUnit\Constraint\Redirect34.php
* funcGetArg
 * Line 111: `        $argv     = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Test\PHPUnit\Constraint\Redirect37.php
* funcGetArg
 * Line 117: `        $argv     = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Test\PHPUnit\Constraint\Redirect41.php
* funcGetArg
 * Line 117: `        $argv     = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Test\PHPUnit\Constraint\ResponseHeader34.php
* funcGetArg
 * Line 120: `        $argv     = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Test\PHPUnit\Constraint\ResponseHeader37.php
* funcGetArg
 * Line 127: `        $argv     = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Test\PHPUnit\Constraint\ResponseHeader41.php
* funcGetArg
 * Line 127: `        $argv     = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Translate\Adapter\Csv.php
* funcGetArg
 * Line 47: `            $args               = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Translate\Adapter.php
* funcGetArg
 * Line 122: `            $args               = func_get_args();`
 * Line 181: `            $args = func_get_args();`
 * Line 530: `            $args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Translate.php
* funcGetArg
 * Line 69: `            $args               = func_get_args();`
 * Line 100: `            $args               = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Validate\Between.php
* funcGetArg
 * Line 95: `            $options = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Validate\Callback.php
* funcGetArg
 * Line 144: `        $args     = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Validate\CreditCard.php
* funcGetArg
 * Line 137: `            $options = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Validate\Date.php
* funcGetArg
 * Line 74: `            $options = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Validate\Db\Abstract.php
* funcGetArg
 * Line 101: `            $options       = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Validate\EmailAddress.php
* funcGetArg
 * Line 132: `            $options = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Validate\File\Count.php
* funcGetArg
 * Line 108: `            $options['min'] = func_get_arg(0);`
 * Line 109: `            $options['max'] = func_get_arg(1);`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Validate\File\Extension.php
* funcGetArg
 * Line 75: `            $case = func_get_arg(1);`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Validate\File\FilesSize.php
* funcGetArg
 * Line 77: `            $argv = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Validate\File\Hash.php
* funcGetArg
 * Line 72: `            $options['algorithm'] = func_get_arg(1);`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Validate\File\ImageSize.php
* funcGetArg
 * Line 122: `            $argv = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Validate\File\Size.php
* funcGetArg
 * Line 106: `            $argv = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Validate\Hostname.php
* funcGetArg
 * Line 1181: `            $options = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Validate\InArray.php
* funcGetArg
 * Line 75: `                $temp['haystack'] = func_get_arg(0);`
 * Line 76: `                $temp['strict']   = func_get_arg(1);`
 * Line 79: `                $temp = func_get_arg(0);`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Validate\Ip.php
* funcGetArg
 * Line 61: `            $options = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Validate\NotEmpty.php
* funcGetArg
 * Line 86: `            $options = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\Validate\StringLength.php
* funcGetArg
 * Line 81: `            $options     = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\View\Abstract.php
* funcGetArg
 * Line 825: `        $args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\View\Helper\DeclareVars.php
* funcGetArg
 * Line 65: `        $args = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\View\Helper\Translate.php
* funcGetArg
 * Line 69: `        $options   = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\View.php
* funcGetArg
 * Line 95: `            include 'zend.view://' . func_get_arg(0);`
 * Line 97: `            include func_get_arg(0);`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\XmlRpc\Request.php
* funcGetArg
 * Line 196: `        $argv = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\library\Zend\XmlRpc\Server.php
* funcGetArg
 * Line 222: `            $argv = func_get_args();`
 * Line 260: `            $argv = func_get_args();`

#### C:\Users\marti\Documents\gambio_tickets75\redesign_modules\versandcountdown\MySql.php
* foreachByReference
 * Line 38: `                foreach ($row as &$value) {`

#### C:\Users\marti\Documents\gambio_tickets75\user_classes\overloads\CheckoutSuccessExtenderComponent\IndivStyleGoogleAnalytics.inc.php
* foreachByReference
 * Line 89: `        foreach ($items as &$item) { `

