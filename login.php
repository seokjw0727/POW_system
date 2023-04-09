<?php
  session_start();
  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];
    // Validate credentials
    if ($username == "admin" && $password == "123") {
      $_SESSION["loggedin"] = true;
      $_SESSION["username"] = $username;
      header("location: welcome.php");
    } else {
      $error = "Invalid username or password";
    }
  }
?>