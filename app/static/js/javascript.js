
/**
 *	Portfolio JavaScript
 *
 *	@author		Andrej Babic
 */

;(function($, Modernizr) {
	"use strict";

	var Bluecap = {
		up: 1,

		init: function () {
			var History = window.History,
				$content = $("#content");
			$("input[placeholder], textarea[placeholder]").placeholder();

			// Ribbon animation
			var $ribbon = $("#ribbon");
			Bluecap.dragRibbon($ribbon);

			// No native support
			if (!Modernizr.cssanimations) {
				var anim_down = function() {
					if (Bluecap.up) $ribbon.animate({top: "10px"}, 500, anim_up);
				};
				var anim_up = function() {
					if (Bluecap.up) $ribbon.animate({top: "-5px"}, 500, anim_down);
				};

				$ribbon.animate({top: "10px"}, 500, anim_up);
			}

		},

		/**
		 * Draggable ribbon
		 */
		dragRibbon: function(el) {
			var _openPos = 210,
				_duration = 400,
				_pos = 0,
				_open = false,
				_startPos = 0,
				_startDelta = 0,
				_container = $(".outer"),
				_handle = el;

			var setPosition = function(pos) {
				_pos = pos;
				pos -= 210;
				_container.animate({ marginTop: pos }, _duration);

				if (_pos == _openPos) {
					_open = true;
					Bluecap.up = 0;
					$("body").removeClass("up");
					_handle.unbind();
				} else if (Bluecap._pos === 0) {
					_open = false;
					_handle.toggleClass("animate");
				}
			};

			_handle.bind("mousedown", function(e) {
					e.preventDefault();
					e.stopPropagation();

					$(this).toggleClass("animate");

					_duration = 0;
					_startPos = _pos = 0;
					_startDelta = e.pageY - _pos;

					$("body").bind("mousemove", mouseMove).bind("mouseup", mouseUp);
			});

			var mouseMove = function(e) {
				var delta = e.pageY - _startDelta;

				if (delta < 0) {
					delta = 0;
				} else if (delta > _openPos) {
					delta = _openPos;
				}

				setPosition(delta);
			};

			var mouseUp = function(e) {
				_handle.toggleClass("animate");
				var strokeLength = _pos - _startPos;
				strokeLength *= strokeLength < 0 ? -1 : 1;

				if (strokeLength > 3) {
					_duration = 200;
					if (_pos == _openPos || !_open) {
						setPosition(_pos > _openPos/2.5 ? _openPos : 0);
					} else {
						setPosition(_pos > _openPos ? _openPos : 0);
					}
				}

				$("body").unbind("mouseup").unbind("mousemove");
			};

		}
	};

	$(document).ready(Bluecap.init);

})(jQuery, Modernizr);
