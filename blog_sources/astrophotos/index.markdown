---
layout: default
---


<div class="grid">
{% for post in site.posts %}
  <div class="grid-item">
    <a href="/astrophotos{{ post.url }}">
      <div class="image-hover">
        <img src="{{ post.photo }}.thumbnail.jpg" alt="{{ post.title }}">
        <div class="image-title">{{ post.title }}</div>
      </div>
    </a>
  </div>
{% endfor %}
</div>

<style>
.grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 20px;
}

.grid-item {
  position: relative;
}
.image-hover {
  /* position: absolute; */
  top: 0;
  left: 0;
  width: 100%;
  height: 100%; 
  overflow: hidden;
}

.image-hover:hover .image-title {
  opacity: 1;
}

.image-title {
  position: absolute;
  bottom: 0;
  left: -10px;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  color: #fff;
  font-size: 14px;
  font-weight: bold;
  padding: 10px;
  opacity: 0;
  transition: opacity 0.3s ease-in-out;
  text-align: center; /* add this line */
} 
</style>
