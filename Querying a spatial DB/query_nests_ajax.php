<?php
    $ls =$_POST['lastsurvey'];
    $rs =$_POST['recentstat'];
    $db = new PDO('pgsql:host = localhost;port=5432;dbname=sdb_course;user=postgres;password=flick95');
    $sql = $db->prepare("SELECT nest_id, lastsurvey, recentstat, ST_AsGeoJSON(ST_Transform(geom,4326),5) FROM raptor_nests WHERE lastsurvey> :ls 
    AND recentstat= :rs ORDER BY nest_id ASC");
    $params = ["ls"=> $ls, "rs"=>$rs];
    $sql->execute($params);
        
    echo "<table class='table table-striped'>";
    echo "<th>nest_id</th>";
    echo "<th>lastsurvey</th>";
    echo "<th>recentstat</th>";
    echo "<th>Geometry</th>";
    while ($row =$sql->fetch(PDO::FETCH_ASSOC)){
            echo "<tr>";
                foreach ($row as $field=>$value){
                        echo "<td>{$value}</td>";
                }   
            echo "</tr>";
    }
    echo "</table";
?>