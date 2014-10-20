$(document).ready(function() {

        $(".name-photo").show(500);
        $("#Home_content").show(500);
        $(".About_post").hide(500);
        $("#Work_Samples_content").hide(500);
        $("#Homing_In_content").hide(500);
        $("#Contact_content").hide(500);

    $("#Home_tab").click(function() {

        $(".name-photo").show(500);
        $("#Home_content").show(500);
        $(".About_post").hide(500);
        $("#Work_Samples_content").hide(500);
        $("#Homing_In_content").hide(500);
        $("#Contact_content").hide(500);

    });

    $("#About_tab").click(function() {

        $(".name-photo").show(500);
        $("#Home_content").hide(500);
        $(".About_post").show(500);
        $("#Work_Samples_content").hide(500);
        $("#Homing_In_content").hide(500);
        $("#Contact_content").hide(500);

    });

     $("#Work_Samples_tab").click(function() {
        $(".name-photo").show(500);
        $("#Home_content").hide(500);
        $(".About_post").hide(500);
        $("#Work_Samples_content").show(500);
        $("#Homing_In_content").hide(500);
        $("#Contact_content").hide(500);

     if ($(".work_samples_style").css("font-size") == "12px" ){
		$(".photo").hide(500);
	}

    });

    $("#Homing_In_tab").click(function() {

        $(".name-photo").hide(500);
        $("#Home_content").hide(500);
        $(".About_post").hide(500);
        $("#Work_Samples_content").hide(500);
        $("#Homing_In_content").show(500);
        $("#Contact_content").hide(500);

     if ($(".graphic").css("margin-left") == "6%" ){
		$("#mock-up").hide(500);
	}

    });

    $("#Contact_tab").click(function() {
        $(".name-photo").hide(500);
        $("#Home_content").hide(500);
        $(".About_post").hide(500);
        $("#Work_Samples_content").hide(500);
        $("#Homing_In_content").hide(500);
        $("#Contact_content").show(500);

    });

});







