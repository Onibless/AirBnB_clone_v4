(document).ready(function () {
  amenity_object = {}
  $("li input[type=checkbox]").change(function () {
    if (this.checked) {
      /* store each checked box in an object */
      amenity_object[this.dataset.name] = this.dataset.id;
    } else {
      /* delete from the object */
      delete amenity_object[this.dataset.name];
    }
    /* modify data of amenities h4 */
    $(".amenities h4").text(Object.keys(amenity_object).sort().join(", "));
  });
});
