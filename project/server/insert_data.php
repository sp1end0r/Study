<?php
    $ID = getenv('DB_ID');
    $PASSWD = getenv('DB_PASSWD');
    $DB_NAME= getenv('DB_NANE');
	$con = mysqli_connect("localhost", $ID, $PASSWD, $DB_NAME);

	if(mysqli_connect_errno())
	{
		echo "Failed to connect to DB ";
		echo " ".mysqli_connect_error();
	}
	
	$data = $_GET['data'];
	$flag = $_GET['flag'];
	$sensor = $_GET['sensor'];
	$query = "INSERT INTO gas_rec (sensor,res,flag) VALUES($sensor,$data,$flag)";
	$res = mysqli_query($con, $query);
	if ($res == false)
	{
		echo mysqli_error($con);
	}

?>