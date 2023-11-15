$("#preorder-form").submit(function () {
  let formValid = true;

  if ($("#preorder-name").prop("validity").valid) {
    $("#feedback-name").addClass("hidden");
  } else {
    $("#feedback-name").removeClass("hidden");
    formValid = false;
  }

  if ($("#preorder-email").prop("validity").valid) {
    $("#feedback-email").addClass("hidden");
  } else {
    $("#feedback-email").removeClass("hidden");
    formValid = false;
  }

  if ($("#preorder-tickets").prop("validity").valid) {
    $("#feedback-tickets").addClass("hidden");
  } else {
    $("#feedback-tickets").removeClass("hidden");
    formValid = false;
  }

  if ($("#preorder-location").prop("validity").valid) {
    $("#feedback-location").addClass("hidden");
  } else {
    $("#feedback-location").removeClass("hidden");
    formValid = false;
  }

  return formValid;
});
