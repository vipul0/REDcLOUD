#!/usr/bin/python2
import cgi, os, extra, commands, cloud

print "Content-Type: text/html"

print "\n\n"

reload(cloud)
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
  <h2 class="text-center">EC2-CONTAINER</h2></br >
    <h4 class="text-center">DOCKER</h4>
  
<!-- Button to open the modal create form -->
<button onclick="document.getElementById('create').style.display='block'">CREATE</button>

<!-- The Modal -->
<div id="create" class="modal">
  <span onclick="document.getElementById('create').style.display='none'"
class="close" title="Close Modal">&times;</span>

  <!-- Modal Content -->
  <form class="modal-content animate" action="Docker.py" method="get">
    <div class="imgcontainer">
      <img src="img_avatar2.png" alt="Avatar" class="avatar">
    </div>

    <div class="container">
<label><b>ENTER NAME ::</b></label><input class="form-control" name="cname" placeholder="CONTAINER NAME" type="text" required><br /><br />

<label><b>FLAVOUR TYPE</b></label>
<select name="imagen" required>
<option value="centos">CENTOS</option>
<option value="Fedora">FEDORA</option>
<option value="ubuntu">UBUNTU</option>
</select>
<br />

      <button type="submit">Launch</button>
	  <button type="button" onclick="document.getElementById('create').style.display='none'" class="cancelbtn">Cancel</button>

    </div>
  </form>
</div>""".format(userid)

print "<div align='center'><h3> MANAGE CONTAINER</h3></hr><br /><br /><table class='table'><th>Image Name</th><th>Container Name</th><th>IP Address</th><th>Status</th><th>Start</th><th>Stop</th><th>Remove</th><th>PAUSE</th><th>RESUME</th><th>Online Shell</th><th>Save Image</th>"

cloud.DockerHandle.Content()

print"</table></div></hr>"

print """<br /><br /><br /><br /></hr><footer class="container-fluid text-center">
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
<script>
function dock_start(cont_name)
{
	document.location='D_Start.py?x=' + cont_name;
}
function dock_stop(cont_name)
{

	document.location='D_Stop.py?x=' + cont_name;
}

function dock_remove(cont_name)
{

	document.location='D_Remove.py?x=' + cont_name;
}
function dock_shell(cont_name)
{

	document.location='D_Shell.py?x=' + cont_name;
}
function dock_save(cont_name)
{

	document.location='D_Save.py?x=' + cont_name;
}
function dock_pause(cont_name)
{

	document.location='D_Pause.py?x=' + cont_name;
}
function dock_unpause(cont_name)
{

	document.location='D_Unpause.py?x=' + cont_name;
}
</script>

</body>
</html>"""
