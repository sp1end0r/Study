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
	
	$query = "SELECT * FROM gas_rec";
	$res = mysqli_query($con, $query);
	if ($res == false)
	{
		echo mysqli_error($con);
	}
	
	echo "<font size=30>". " Sensor / Measure / Detection ";
	while($row = mysqli_fetch_array($res)){
		echo "<font size=30>"."<p>"."/".$row['sensor']."/".$row['res']."/".$row['flag']."/"."</p>";
	}

?>