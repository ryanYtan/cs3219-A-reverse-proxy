<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <img v-bind:src="imgsrc" />
    <h1>This guy's name is {{ imgcap }}</h1>
  </div>
</template>

<script>
import axios from "axios";

export default {
    name: "HelloWorld",

    props: {
        msg: String
    },

    data() {
        return {
            imgsrc: "",
            imgcap: ""
        };
    },

    async mounted() {
        const { name } = (await axios.get("http://localhost/namer")).data;
        this.name = name;
        const {
            imgsrc, imgcap
        } = (await axios.get(`http://localhost/imager?name=${this.name}`)).data;
        this.imgsrc = imgsrc;
        this.imgcap = imgcap;
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
