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
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<style>{0}</style>
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
<li><a href="saas.py">SOFTWARE</a></li>
<li><a href="efs.py">EFS</a></li>
<li><a href="ec2.py">EC2</a></li>
<li><a href="kub.py">VPC</a></li>
<li><a href="ebs.py">EBS</a></li>
<li><a href="#">EC2 CONTAINER</a></li>
<li><a href="paas.py">PLATFORM</a></li>

</ul>
</li>     
</ul>

<ul class="nav navbar-nav navbar-right">
<li><a href="#"><span class="glyphicon glyphicon-user"></span>{0}</a></li>
<li><a href="logout.py"><span class="glyphicon glyphicon-log-in"></span>LOGOUT</a></li>
</ul>
</div>
</nav>
""".format(userid)


print """<div class='columns'>
<ul class="sertyp">
    <li class="header">SOFTWARE</li>
    <li class="grey"><spam> <img src='images/raw_software.png' /></span></li>
    <li class="grey"><a href='saas.py'>Discover</a></li>
  </ul>
</div>

<div class='columns'>
<ul class="sertyp">
    <li class="header">STORAGE</li>
    <li class="grey"><spam> <img src='images/raw_storage.png' /></span></li>
    <li class="grey"><a href='staas.py'>Discover</a></li>
  </ul></div>
<div class='columns'>
<ul class="sertyp">
    <li class="header">CONTAINER</li>
    <li class="grey"><spam> <img src='images/raw_software.png' /></span></li>
    <li class="grey"><a href='caas.py'>Discover</a></li>
  </ul>
</div>
<div class='columns'>
<ul class="sertyp">
    <li class="header">PLATFORM</li>
    <li class="grey"><spam> <img src='images/raw_software.png' /></span></li>
    <li class="grey"><a href='paas.py'>Discover</a></li>
  </ul>
</div>
<div class='columns'>
<ul class="sertyp">
    <li class="header">INFRASTRUCTURE</li>
    <li class="grey"><spam> <img src='images/raw_software.png' /></span></li>
    <li class="grey"><a href='ec2.py'>Discover</a></li>
  </ul>
</div>

<div class='columns'>
<ul class="sertyp">
    <li class="header">VPC</li>
    <li class="grey"><spam> <img src='images/raw_software.png' /></span></li>
    <li class="grey"><a href='kub.py'>Discover</a></li>
  </ul>
</div>

</body>
</html>"""
