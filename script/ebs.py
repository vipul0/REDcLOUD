#!/usr/bin/python2
import cgi, os, extra, commands, cloud

print "Content-Type: text/html"

print "\n\n"

cs0, cs1=extra.rawcss()
js=extra.rawjs()

x=os.environ["HTTP_COOKIE"].split()
y=x[0].split("=")
userid=y[1]

print """<!DOCTYPE html>
<html lang="en">
<head>
	<title>REDcLOUD</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script><style>{0}</style>
<style>{1}</style>
<script>{2}</script>""".format(cs0, cs1, js)
	
print """</head>
<body id="body_default">
<nav class="navbar navbar-inverse">
<div class="container-fluid">
<div class="navbar-header">
<a class="navbar-brand" href="Home.html">REDcLOUD</a>
</div>
<ul class="nav navbar-nav">
<li class="dropdown">
<a class="dropbtn" >SERVICES<span class="caret"></span></a>
<ul class="dropdown-content">
<li><a href="#">SOFTWARE</a></li>
<li><a href="#">EFS</a></li>
<li><a href="#">EC2</a></li>
<li><a href="#">VPC</a></li>
<li><a href="#">EBS</a></li>
<li><a href="#">EC2 CONTAINER</a></li>
<li><a href="#">PLATFORM</a></li>

</ul>
</li>     
</ul>

<ul class="nav navbar-nav navbar-right">
<li><a href="#"><span class="glyphicon glyphicon-user"></span>{0}</a></li>
<li><a href="#"><span class="glyphicon glyphicon-log-in"></span>LOGOUT</a></li>
</ul>
</div>
</nav>
<div id="container" class="container-fluid bg-grey">
  <h2 class="text-center">ELASTIC BLOCK STORAGE</h2></br >
    <h4 class="text-center">ISCSI PROTOCOL</h4>
  
  
   
   <!-- Button to open the modal login form -->
<button onclick="document.getElementById('create').style.display='block'">CREATE</button>

<!-- The Modal -->
<div id="create" class="modal">
  <span onclick="document.getElementById('create').style.display='none'"
class="close" title="Close Modal">&times;</span>

  <!-- Modal Content -->
  <form class="modal-content animate" action="/script/iscsi.py" method="get">
    <div class="imgcontainer">
      <img src="img_avatar2.png" alt="Avatar" class="avatar">
    </div>

    <div class="container">
      <label><b>SIZE</b></label>
      <input class="form-control"  name="Bsize" placeholder="SIZE OF STORAGE IN GB" type="number" min="1" max="20" required>
<br />
<br />
      <label><b>NAME</b></label>
      <input class="form-control" name="fnm" placeholder="Name" type="text" required>
<br />
<br />	  
	  <label><b>ID NO.</b></label>
      <input class="form-control" name="idnm" placeholder="Id Name" type="number" required>
<br />
<br />
<br />
      <button type="submit">CREATE</button>
	  <button type="button" onclick="document.getElementById('create').style.display='none'" class="cancelbtn">Cancel</button>

    </div>
  </form>
</div>""".format(userid)

print """<div class="container">
  <h2>BLOCK STORAGE TABLE</h2>
  <p>Here you can create a new partiton or you ca delete a pre create block storage.</p>

<br />
<br />
  
  <table class="table">
    <thead>
      <tr>
        <th>NAME</th>
        <th>SIZE</th>
        <th>USED</th>
		<th>IQN</th>
		<th>BACKUP</th>
      """


cloud.ScsiHandle.ManageMatter()


print """</tr>
    </thead>
    <tbody>
  </table>
</div>
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />

<footer class="container-fluid text-center">
  <a href="#myPage" title="To Top">
    <span class="glyphicon glyphicon-chevron-up"></span>
  </a>
  <p>REDcLOUD Pvt.Ltd. <a href="Home.py" title="Visit REDcLOUD">REDcLOUD</a></p>
</footer>

 <script>
// Get the modal
var modal = document.getElementById('create');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {

    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
</script> 

</body>
</html>"""
