<template>
      <footer>
        <div style="background-color:rgb(230, 230, 230); font-size: 13px; ">
          <div style="text-align:center;  margin-top:20px; color:grey">
            <div style="padding-top: 5px; padding-bottom: 2px;">무비헤엄🌊</div>
            <div style="padding-bottom: 2px;">SSAFY 10기</div>
            <div class="name" style="width:12.5%; font-size: 15px;">Yeongjun Ryu | Jisu Seo</div>
            <div style="padding-top: 2px; padding-bottom: 10px;">© 2023 All Rights Reserved.</div>
          </div>
        </div>
      </footer>
    </template>
    
    <script>
    export default {
      name: 'FootBar',
      data() {
        return {
        }
      }
    
    }
    </script>
    
    <style scoped>
    
     .name{
      background: linear-gradient(45deg, #9a9ae3, #ba68ed);
      animation: hue-rotate 2s linear infinite alternate;
      color: rgb(26, 26, 26);
      border-radius: 5px;
      display: inline-block;
    }
    
    @keyframes hue-rotate {
      to{ filter: hue-rotate(90deg)}
    }
    
    </style>