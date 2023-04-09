<?php
  session_start();
  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];
    // Check if username and password are correct
    if ($username == "admin" && $password == "123") {
      $_SESSION["loggedin"] = true; 
      $_SESSION["username"] = $username;
      header("location: welcome.html"); # Redirect to welcome page
    } else {
      $error = "Invalid username or password"; # Error message
    }
  }
?>