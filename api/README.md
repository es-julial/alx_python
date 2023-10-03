# API

![screenshot](https://zupimages.net/up/23/40/syi7.png)

  


<div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <h2>Background Context</h2>

<p><a href="https://youtu.be/-2kyU6-j8ZQ" target="_blank"><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/897638f42eb1bad6605d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230930%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230930T132722Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b632417793b28cbef18101f8103c721a9dc988a0bd0acb6274b9b4a4ba352bb3" alt="" loading='lazy' style="" /></a></p>

<p>Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.</p>

<p>One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them &ndash; access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.</p>

<p>This is a perfect example of a task that is not suited for Bash scripting, so let&rsquo;s build Python scripts.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/CRB8vFQ4CMWEDGoXxe9xIA" title="What is an API" target="_blank">What is an API</a> </li>
<li><a href="/rltoken/nmdvTgdZH9JCSNJo19sA0Q" title="What is an API? In English, please" target="_blank">What is an API? In English, please</a></li>
<li><a href="/rltoken/2bfOp8WycFmfCeion6vx4A" title="What is a REST API" target="_blank">What is a REST API</a> </li>
<li><a href="/rltoken/rZbEFi14t48LMjdYzWyqEQ" title="What are microservices" target="_blank">What are microservices</a> </li>
<li><a href="/rltoken/maJqoGCnAPzDho1WsQSEfw" title="PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry" target="_blank">PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/hGnr6mo-f4McEnO1RMC0WA" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is an API</li>
<li>What is a REST API</li>
<li>What are microservices</li>
<li>What is the CSV format</li>
<li>What is the JSON format</li>
<li>Pythonic Package and module name style</li>
<li>Pythonic Class name style</li>
<li>Pythonic Variable name style</li>
<li>Pythonic Function name style</li>
<li>Pythonic Constant name style</li>
<li>Significance of CapWords or CamelCase in Python</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Recommended editors: <code>Visual studio code</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li><strong>Libraries imported in your Python files must be organized in alphabetical order</strong></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>You must use <a href="/rltoken/Wvntvx6slm5JXocswoOIFA" title="get" target="_blank">get</a> to access to dictionary value by key (it won&rsquo;t throw an exception if the key doesn&rsquo;t exist in the dictionary)</li>
<li>Your code should not be executed when imported (by using <code>if __name__ == &quot;__main__&quot;:</code>)</li>
</ul>

  </div>
</div>