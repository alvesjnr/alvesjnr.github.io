---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

# layout: home
# ---

# ---
layout: default
# title: My Blog
---

<div class="post-grid">
  {% for post in site.posts %}
    <div class="post">
      <a href="/astrophotos{{ post.url }}">
        <img src="{{ post.photo }}" alt="{{ post.title }}" />
        <h2>{{ post.title }}</h2>        
      </a>
    </div>
  {% endfor %}
</div>

<style>
  .post-grid {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 20px;
  }

  .post {
    position: relative;
  }

  .post img {
    max-width: 100%;
    height: auto;
  }

  .post h2 {
    position: absolute;
    bottom: 10;
    left: 0;
    width: 100%;
    background-color: rgba(0, 0, 0, 0.8);
    color: #fff;
    padding: 10px;
    margin: 0;
    text-align: center;
    font-size: 0.8rem;
    font-weight: 400;
    text-decoration: none;
  }

  .post h2:hover {
    background-color: rgba(0, 0, 0, 0.5);
    color: #fff;
  }
</style>