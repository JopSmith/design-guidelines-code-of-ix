# Design Basics

**Date:** 10/09/2026  
**Version:** 1.0  
**Author:** Jonathan Smith

## Introduction

Basics defines the foundational standards that every intelligent experience should meet.

These guidelines turn broader principles into clear, practical rules for creating consistent, accessible and usable experiences across products, platforms and contexts.

They provide a shared baseline for quality and inform the more detailed techniques in Tactics.

### Contents

01. [Accessibility](#01-accessibility)
02. [Actions and buttons](#02-actions-and-buttons)
03. [Content and language](#03-content-and-language)
04. [Dialogs and overlays](#04-dialogs-and-overlays)
05. [Feedback and system status](#05-feedback-and-system-status)
06. [Forms and validation](#06-forms-and-validation)
07. [Icons and iconography](#07-icons-and-iconography)
08. [Interaction and motion](#08-interaction-and-motion)
09. [Layout and responsive design](#09-layout-and-responsive-design)
10. [Navigation and disclosure](#10-navigation-and-disclosure)
11. [Tables and data](#11-tables-and-data)

---

## 01. Accessibility

### Label icons that may be unclear
<small>IX-BASIC-A11Y-001<small>

Use icon-only controls only when the icon’s meaning is familiar and unambiguous, such as a pencil for Edit. Pair less familiar icons with clear text labels, and always provide an accessible name for assistive technology

### IX-BASIC-A11Y-002 - Don’t rely on colour alone

Avoid using colour as the only way to distinguish states, groups or categories. Colour can be difficult to remember or perceive and may create accessibility barriers. Use clear labels, icons or other identifiers alongside colour to communicate meaning.

### IX-BASIC-A11Y-003 - Use accessible touch targets

Give buttons, links and interactive controls a touch target of at least 44 × 44px on mobile. Do not apply this minimum to desktop layouts — use the design-system’s default component height there and increase to 44px at the mobile breakpoint only.

### IX-BASIC-A11Y-004 - Maintain contrast for muted text

Ensure muted text still has sufficient contrast against its background to remain easy to read. Use reduced emphasis without compromising legibility, particularly for users with low vision or other visual impairments.

### IX-BASIC-A11Y-005 - Keep keyboard focus visible

Use clear, visible focus rings on interactive elements so keyboard users can always identify where focus is. Ensure focus indicators remain distinct across backgrounds and states without relying on colour alone.

### IX-BASIC-A11Y-006 - Don’t rely on tooltips for important info

Use tooltips only for supplementary guidance. Important information should remain visible or accessible without hover, as tooltips can be missed, are difficult to discover and may not work reliably on touch devices.

### IX-BASIC-A11Y-007 - Move focus to meaningful content

After opening a dialog, navigating to a new step or displaying an important error, move keyboard focus to the most relevant location so users can continue without searching for where the interface changed.

### IX-BASIC-A11Y-008 - Return focus after closing overlays

When a dialog, drawer or other overlay closes, return keyboard focus to the control that opened it. This preserves context and helps keyboard and assistive technology users continue their task.

### IX-BASIC-A11Y-009 - Keep focus inside modal dialogs

While a modal dialog is open, keep keyboard focus within it until dismissal. Prevent users from reaching inactive content behind the modal, and ensure focus moves to a logical control when the dialog opens.

### IX-BASIC-A11Y-010 - Support keyboard controls

Ensure every interactive control can be reached and operated with a keyboard. Do not rely solely on mouse movement, hover, dragging or touch gestures, as these may exclude keyboard and assistive technology users.

### IX-BASIC-A11Y-011 - Don’t use hover as the only interaction

Make essential controls and information available without hover. Hover can provide additional feedback, but touch and keyboard users must still be able to discover and access the same content and functionality.

### IX-BASIC-A11Y-012 - Support text resizing

Ensure layouts remain usable when users increase text size. Content should reflow without clipping, overlapping controls or unnecessary horizontal scrolling. Preserve readable spacing, clear hierarchy and sufficiently large interaction targets so users can continue working comfortably.

### IX-BASIC-A11Y-013 - Keep interactive elements distinct

Make buttons, links, inputs and other controls recognisable as interactive. Avoid styling interactive and non-interactive elements so similarly that users must experiment to understand what can be clicked or activated.

### IX-BASIC-A11Y-014 - Respect reduced-motion preferences

Reduce or remove non-essential animation when users enable a reduced-motion preference. Preserve necessary feedback with simpler transitions or immediate state changes so changes remain understandable without motion that may cause discomfort or interfere with task completion.

### IX-BASIC-A11Y-015 - Keep headings in a logical hierarchy

Use heading levels in structural order rather than choosing them for visual size alone. Move sequentially, such as H2 to H3 rather than H2 to H4, so visual and assistive technology users can understand page organisation.

### IX-BASIC-A11Y-016 - Write descriptive link text

Use meaningful link labels that describe their destination or purpose, even out of context. Avoid vague phrases such as “Click here” or “Read more”. Specific wording helps users scan links and understand where they lead.

---

## 02. Actions and buttons

### IX-BASIC-ACTION-001 - Use button groups for actions

Use button groups for actions that affect the current content, such as applying filters, changing formatting or selecting display options. Don’t use them to switch between related views or datasets, as tabs provide a clearer and more familiar navigation pattern.

### IX-BASIC-ACTION-002 - Limit primary actions to one per page

Limit each page to a single primary action so the most important next step is clear and easy to identify. Use secondary or tertiary actions for supporting tasks to maintain hierarchy and avoid competing calls to action.

### IX-BASIC-ACTION-003 - Iconise the primary action

Use a leading icon only on the page’s primary action, where the icon reinforces its meaning. Keep secondary actions text-only to reduce visual noise, preserve hierarchy and make the most important action easier to identify.

### IX-BASIC-ACTION-004 - Use Add for create actions

Use an Add label with a leading plus icon for primary actions that create something. This provides a clear, familiar pattern and makes the outcome explicit. Avoid New, which can be less specific and may imply unproven.

### IX-BASIC-ACTION-005 - Order actions by priority

Arrange buttons from right to left, beginning with the primary or most positive action and progressing towards less prominent actions. Place Cancel or Close at the opposite end to maintain predictable hierarchy and distinguish dismissal from progression.

### IX-BASIC-ACTION-006 - Highlight the primary action 

Use a primary-coloured button for the main action on a page to make it visually distinct from secondary actions. This reinforces hierarchy, draws attention to the preferred next step and stops actions from competing.

### IX-BASIC-ACTION-007 - Highlight destructive actions

Use a destructive-coloured button for actions with negative or irreversible consequences. This clearly communicates risk, distinguishes them from routine actions and helps users recognise when extra care is needed to proceed.

### IX-BASIC-ACTION-008 - Don’t use Close to discard changes

Use Close to dismiss dialogs, drawers, screens or applications without validation or implying data loss. When a form contains unsaved changes, use an explicit discard or cancel action so users understand the consequence before leaving.

### IX-BASIC-ACTION-009 - Use Cancel to discard form changes

Use Cancel to stop an in-progress form, discard unsaved changes and return users to the previous state. This makes the outcome clear and distinguishes cancelling a process from simply closing or dismissing an interface.

### IX-BASIC-ACTION-010 - Limit page header actions

Keep page headers to a maximum of four buttons to maintain clarity and avoid overcrowding. If additional actions are needed, use the fourth button as a More menu and place lower-priority options within it.

### IX-BASIC-ACTION-011 - Indicate additional actions clearly

Use a trailing three-vertical-dots icon on More or overflow buttons to signal that additional actions are available. Where space is limited, use an icon-only button while ensuring its purpose remains clear and accessible.

### IX-BASIC-ACTION-012 - Keep Add terminology consistent

When an Add action opens a dialog, drawer or page, continue using Add in the title and primary action. Avoid switching to Create or other terminology, as consistent labels make the flow clearer and more predictable.

### IX-BASIC-ACTION-013 - Use Save to confirm edits

When an Edit action opens a dialog, drawer or page, use Edit in the title and Save as the primary action. This keeps terminology clear by distinguishing the task being performed from the action that confirms the changes.

### IX-BASIC-ACTION-014 - Use one accent colour per screen

Avoid placing differently coloured primary, success and destructive buttons side by side. Use one dominant accent for routine hierarchy, and reserve destructive colour for contexts where risk is the primary message, such as a destructive confirmation or dedicated action.

### IX-BASIC-ACTION-015 - Safeguard destructive actions

Protect destructive or irreversible actions with a safeguard appropriate to their impact. Use confirmation messages when consequences cannot be easily reversed. Where safe reversal is possible, consider Undo instead so routine actions remain efficient without risking accidental loss.

### IX-BASIC-ACTION-016 - Adapt page header actions for mobile

On mobile, collapse three or more page header actions into an overflow menu to reduce crowding. When only one or two actions are needed, icon-only buttons are acceptable where the icons are familiar, unambiguous and accessible.

### IX-BASIC-ACTION-017 - Don’t disable primary actions

Keep primary actions enabled wherever possible and validate when users attempt to continue. Disabled actions can be difficult to discover and may leave users unclear about what is preventing them from progressing.

### IX-BASIC-ACTION-018 - Keep destructive actions separated

Separate destructive actions from frequently used positive actions when accidental activation is possible. Use spacing, hierarchy or an overflow menu to reduce mis-clicks and make the higher-risk action visually distinct without giving it unnecessary prominence.

### IX-BASIC-ACTION-019 - Offer Undo for reversible actions

When an action can safely be reversed, consider providing a temporary Undo option instead of asking for confirmation beforehand. This keeps routine interactions fast while still allowing users to recover from mistakes.

### IX-BASIC-ACTION-020 - Avoid unnecessary confirmations

Don’t ask users to confirm routine, low-risk actions, as unnecessary prompts interrupt their flow and slow down common tasks. Reserve confirmation for destructive, irreversible or consequential actions where accidental activation would have a meaningful impact.

### IX-BASIC-ACTION-021 - Keep button labels concise

Keep button labels to one word wherever possible, using clear actions such as Add, Save or View. Avoid repeating context already provided by the page or form. Use a second word only when the action would otherwise be genuinely ambiguous.

---

## 03. Content and language

### IX-BASIC-CONTENT-001 - Communicate purpose with titles

Give every page a clear title and, where useful, a supporting subtitle that establishes context and purpose. Consistent page headings strengthen visual hierarchy, improve orientation and help users understand where they are and what the page is for.

### IX-BASIC-CONTENT-002 - Keep subtitles free of full stops

Avoid ending short subtitles with a full stop. Treating subtitles like interface labels rather than body copy creates a clean, consistent heading style and encourages concise supporting text. Only use punctuation when subtitles contain multiple sentences.

### IX-BASIC-CONTENT-003 - Use sentence case for labels

Always write labels in sentence case to improve readability and maintain consistency across the interface. Only use title casing when required for proper names, product names or other branded terms.

### IX-BASIC-CONTENT-004 - Avoid unnecessary abbreviations

Use abbreviations sparingly and spell out words in full wherever space allows. Clear, familiar language is easier to understand and reduces ambiguity, particularly for users who may not recognise shortened terms. For example, use Hour instead of Hr.

### IX-BASIC-CONTENT-005 - Avoid unnecessary acronyms

Use acronyms and initialisms sparingly and spell out the full phrase wherever practical. When shortened forms are necessary, use capital letters without full stops and apply them consistently. For example, use WIP instead of W.I.P.

### IX-BASIC-CONTENT-006 - Avoid using ampersands

Use “and” instead of an ampersand (&) wherever possible. Writing the word in full improves readability, reduces ambiguity and provides a more reliable experience for people using screen readers or other assistive technologies.

### IX-BASIC-CONTENT-007 - Use bold text sparingly

Avoid bold text for emphasis, as it can disrupt reading flow and appear visually cluttered. Use italics or an accessible colour treatment instead. However, bold text is appropriate for headings, subheadings, and lead text in bullet points.

### IX-BASIC-CONTENT-008 - Avoid all-capital text

Avoid using all capitals for sentences, labels or longer text. All-capital text is harder to scan, can reduce readability and may feel overly forceful. Use sentence case instead to create a clearer, more consistent reading experience.

### IX-BASIC-CONTENT-009 - Use consistent terminology

Use the same words for the same concepts and actions throughout the product. Consistent terminology helps users recognise patterns, understand instructions more quickly and avoid confusion. For example, don’t alternate between Add and Create for the same action.

### IX-BASIC-CONTENT-010 - Check spelling before release

Check spelling throughout the interface before release. Spelling errors can reduce clarity, create confusion and undermine trust in the quality of the product. Consistent, accurate language helps maintain a credible and professional user experience.

### IX-BASIC-CONTENT-011 - Reserve underlining for links

Avoid underlining text for emphasis or decoration, as users may mistake it for an interactive link. Reserve underlining for genuine links to keep interactive elements clear, familiar and easy to recognise.

### IX-BASIC-CONTENT-012 - Choose the right date format

Use absolute dates when precision or comparison matters, and relative dates when recency is more useful. Make relative dates progressively more specific as they age, then switch to an absolute date once relative wording is no longer helpful, e.g. “Just now” to “1 day ago” to “4 Sep 2026”.

### IX-BASIC-CONTENT-013 - Balance headings and line breaks

Keep headings visually balanced and body copy wrapping cleanly. Avoid awkward breaks, trailing words or single words stranded on the final line, as intentional line lengths improve readability, rhythm and overall visual quality.

### IX-BASIC-CONTENT-014 - Truncate long titles in small spaces

Truncate long titles when space is limited to prevent wrapping, crowding or layout disruption. Keep enough text visible to preserve meaning and provide access to the full title where needed.

### IX-BASIC-CONTENT-015 - Keep body text lines readable

Keep body text to around 60–75 characters per line. Shorter line lengths reduce eye movement, make it easier to find the start of the next line and create a calmer, more comfortable reading rhythm.

---

## 04. Dialogs and overlays

### IX-BASIC-OVERLAY-001 - Avoid stacking dialogs

Opening a dialog on top of another can confuse users, obscure context and create accessibility issues. Keep users within one clear flow by updating the current dialog, closing it first or moving complex tasks to a dedicated page.

### IX-BASIC-OVERLAY-002 - Don’t interrupt users unnecessarily

Allow users to view and understand a page before showing pop-ups, dialogs or overlays. Interrupting too early obscures context, disrupts task flow and increases the likelihood that users will dismiss the message or abandon the experience.

### IX-BASIC-OVERLAY-003 - Use dialogs for focused content

Keep dialogs focused on concise, task-specific content. Avoid overloading them with complex information or interactions. When more space, context or navigation is needed, consider using a drawer or full page instead.

### IX-BASIC-OVERLAY-004 - Keep data tables out of dialogs

Avoid presenting data tables within dialogs, as limited space can make complex information harder to scan, navigate and interact with. Use a drawer or full page when users need to review or work with tabular data.

### IX-BASIC-OVERLAY-005 - Keep scrolling within the dialog body

When dialog content exceeds the available height, the dialog body should control scrolling. Avoid nested scroll areas within forms or other content, as they make interaction harder and create an inconsistent experience.

### IX-BASIC-OVERLAY-006 - Use solid modal backdrops

Use a solid backdrop behind modals instead of background blur. Solid backdrops reduce rendering overhead while keeping enough surrounding context visible for users who may need to reference information behind the modal.

### IX-BASIC-OVERLAY-007 - Preserve context in supporting content

Use dialogs, drawers or expandable regions for supporting tasks when users benefit from retaining page context. Use a new page when the task requires substantial space, navigation or independent focus.

### IX-BASIC-OVERLAY-008 - Don’t obscure required context

Avoid placing dialogs, drawers or other overlays over information users need to reference while completing a task. If important context must remain visible, reposition or resize the overlay, use a side drawer, or move the task to a dedicated page.

---

## 05. Feedback and system status

### IX-BASIC-FEEDBACK-001 - Only use call-to-actions for recovery

Don’t add a call-to-action to every empty state. Only use one when there is a clear, useful next step, such as clearing filters, resetting a search or adding an item. Otherwise, concise guidance is often enough.

### IX-BASIC-FEEDBACK-002 - Notify of background activity

Use a brief top-right aligned notification (Toast component) to confirm the success or failure of background activities, such as the import of users. The notification should appear and dismiss automatically without interrupting the user’s workflow, with an optional dismiss action when needed.

### IX-BASIC-FEEDBACK-003 - Notify of immediate feedback

Use a brief bottom-centre aligned notification (Toast component) to confirm success or failure immediately after a user action, such as updating a password. The notification should appear and dismiss automatically without disrupting the workflow, with an optional dismiss action when needed.

### IX-BASIC-FEEDBACK-004 - Notify of system messages

Place persistent system messages, such as system downtime advisory, at the top of the page, dialog, drawer or form they affect (Alert component). Use them for important states that may influence usage or availability, with an optional dismiss action where appropriate.

### IX-BASIC-FEEDBACK-005 - Match loading states to content

Use loading skeletons that reflect the structure and dimensions of the content they replace. This reduces layout shift and helps users anticipate what is loading. Avoid spinners where a meaningful skeleton can provide clearer progress feedback.

### IX-BASIC-FEEDBACK-006 - Keep error messages actionable

Write error messages in clear, human language that explains what went wrong and how to fix it. Avoid generic wording, implementation details and technical codes unless users genuinely need them to diagnose the problem or recover.

### IX-BASIC-FEEDBACK-007 - Show progress for longer processes

Provide clear progress feedback when an operation takes a noticeable amount of time. Use a progress bar when you can show how much is complete and explain what is happening when exact progress is unavailable.

### IX-BASIC-FEEDBACK-008 - Make empty states reflect the cause

Tailor each empty state to its cause, such as first use, no search results, active filters or completed work. Explain why content is unavailable and, where useful, provide guidance or an action that helps users continue.

### IX-BASIC-FEEDBACK-009 - Keep success messages concise

Confirm successful actions briefly and clearly, stating what happened without repeating information the user already knows. Avoid adding extra instructions or follow-up actions unless they are genuinely required, so success feedback remains useful without interrupting progress.

---

## 06. Forms and validation

### IX-BASIC-FORM-001 - Use switches for immediate settings

Use switches for settings that take effect immediately when turned on or off, e.g. enabled/disabled. Their clear on/off state helps users understand the outcome of their action and distinguishes them from checkboxes, which support selection, or buttons, which trigger actions.

### IX-BASIC-FORM-002 - Give filters a clear default state

Use clear default options such as “Select…” or “Sort by…” to communicate what the filter does and what action is expected. This helps users understand the control before making a selection and keeps filter behaviour consistent.

### IX-BASIC-FORM-003 - Allow only one radio selection

Allow only one radio button to be selected within a group. Selecting a different option must automatically deselect the previous one. This ensures users understand that radio buttons are for mutually exclusive choices and keeps selection behaviour clear and predictable.

### IX-BASIC-FORM-004 - Allow multiple checkbox selections

Allow multiple checkboxes to be selected within a group. Selecting one option must not deselect any others. This ensures users understand that checkboxes support independent or multiple choices and keeps selection behaviour clear and predictable.

### IX-BASIC-FORM-005 - Size fields to match expected input

Size form fields according to the type and length of content users are expected to enter. Appropriate field widths provide useful visual cues, improve scannability and help users understand the expected input before they begin typing.

### IX-BASIC-FORM-006 - Use wizards for sequential steps

Use a wizard when users need to complete a task through a defined sequence of steps. Breaking the process into smaller stages reduces cognitive load, clarifies progress and helps users focus on one decision at a time.

### IX-BASIC-FORM-007 - Allow disabled fields to be enabled

Only show fields as disabled when another interaction can make them available. This helps users understand that the field is temporarily unavailable and may become editable, rather than presenting controls they can never use.

### IX-BASIC-FORM-008 - Don’t mark read-only fields as required

Don’t show mandatory indicators against read-only fields. Required states are only relevant when users can enter or change information, so removing them avoids confusion and keeps the purpose of read-only content clear.

### IX-BASIC-FORM-009 - Avoid placeholder text

Do not use placeholder text for essential labels or instructions because it disappears during input and may not be announced by screen readers reliably. Use persistent labels and help text. Placeholders may supplement these only for concise format examples or prompts.

### IX-BASIC-FORM-010 - Place form actions below the form

Place form actions directly beneath the form to create a clear completion point. This follows the natural flow of entering information before taking action and keeps form layouts consistent and easy to scan.

### IX-BASIC-FORM-011 - Align form actions responsively

Right-align form footer buttons by default to create a consistent completion point at the end of the form. However, on smaller devices, make the buttons full width so they are easier to reach, tap and scan within narrow layouts. For example ← space → Cancel | Save by default and Cancel | Save on mobile

### IX-BASIC-FORM-012 - Pair submit actions with Cancel

Always place a Cancel button immediately to the left of a form’s primary submit action, such as Add or Save. This gives users a clear way to abandon changes and keeps form action order consistent and predictable. For example ← space → Cancel | Save

### IX-BASIC-FORM-013 - Use auto-save for lightweight changes

Use auto-save for low-risk changes such as settings, preferences, profile information and drafts. Saving changes as they happen reduces unnecessary actions, supports faster task completion and helps users avoid losing work.

### IX-BASIC-FORM-014 - Use Save for high-impact changes

Use an explicit Save action for complex forms, sensitive settings and other high-impact changes. This gives users a clear opportunity to review information before committing and helps prevent unintended updates.

### IX-BASIC-FORM-015 - Use Submit or Publish for final actions

Auto-save progress during longer workflows, but use an explicit Submit or Publish action when users are ready to make changes final. This clearly separates saving work in progress from committing a consequential outcome.

### IX-BASIC-FORM-016 - Order Select options alphabetically

Arrange the options in a Select alphabetically to make lists predictable and easier to scan. For longer lists, optionally include search to help users find the option they need more quickly without manually scanning the full list.

### IX-BASIC-FORM-017 - Indicate required or optional fields

Mark required fields with an asterisk when most fields are optional, and explain the indicator at the start of the form, such as “* Required fields”. If most fields are required, label the fewer optional fields with “(optional)” instead.

### IX-BASIC-FORM-018 - Show errors next to their fields

Place each validation error directly below the field it relates to. Keeping feedback close to the source makes errors easier to understand, helps users identify what needs fixing and supports faster recovery.

### IX-BASIC-FORM-019 - Give every form field a visible label

Provide a persistent, visible label for every form field so users can understand what information is required. Never rely on placeholder text as the only label, as it disappears during input and isn’t always announced by screen readers.

### IX-BASIC-FORM-020 - Use single-column forms

Arrange form fields in a single column wherever possible. A linear layout creates a clear reading and completion order, reduces eye movement and makes forms easier to scan, complete and navigate across different screen sizes.

### IX-BASIC-FORM-021 - Display read-only values as text

Present read-only information as plain text rather than using default or disabled field styling. This clearly distinguishes fixed information from editable or temporarily unavailable controls and reduces ambiguity about whether users can interact with it or not.

### IX-BASIC-FORM-022 - Place related fields together

It’s acceptable to place closely related fields next to each other when it improves comprehension and completion, such as first name and last name. However, keep the relationship clear and avoid multi-column layouts for fields that are not naturally connected.

### IX-BASIC-FORM-023 - Use Selects for longer option lists

Use a Select for six or more options to keep longer lists compact and manageable. Use a Radio Group when users choose between one and five options, so every choice remains visible and easy to compare.

### IX-BASIC-FORM-024 - Allow read-only text to be copied

Keep read-only text selectable so users can copy values when needed. Preventing selection adds unnecessary friction, particularly for reference information such as IDs, addresses, codes or other details users may need.

### IX-BASIC-FORM-025 - Preserve user input after validation

Keep previously entered values when validation fails. Users should only need to correct fields with errors, rather than re-entering information they have already provided. Preserving input reduces frustration and makes recovery faster.

### IX-BASIC-FORM-026 - Differentiate disabled controls clearly

Style disabled controls so they are distinguishable from enabled controls without making their labels difficult to read. Users should understand what the control does, even when it is temporarily unavailable.

### IX-BASIC-FORM-027 - Validate at the right time

Avoid showing validation errors before users have had an opportunity to complete a field. Validate after meaningful interaction, such as leaving the field or submitting the form, and provide feedback close to the input.

### IX-BASIC-FORM-028 - Summarise form errors when needed

For forms with multiple errors, provide an error summary near the top alongside field-level messages. Include links to affected fields so users can move directly from the summary to fix each problem.

### IX-BASIC-FORM-029 - Keep labels close to their controls

Position labels consistently and close to the controls they describe. Clear proximity strengthens the relationship between label and input and reduces the chance of users associating a label with the wrong field.

### IX-BASIC-FORM-030 - Group related form fields semantically

Use clear section headings or fieldsets to group related inputs within longer forms. Semantic grouping provides context, improves scanning and helps assistive technology users understand relationships between controls, navigate and interpret complex forms more effectively.

### IX-BASIC-FORM-031 - Provide help separately from labels

Keep field labels concise and place help text or formatting guidance in supporting text. Separating instructions from labels makes forms easier to scan and helps assistive technology users interpret each field clearly.

### IX-BASIC-FORM-032 - Prevent duplicate submissions

Prevent repeated activation while a request is processing. Give immediate feedback that the action has been received, then temporarily disable or otherwise guard the initiating control until processing completes so users cannot accidentally submit the same request twice.

### IX-BASIC-FORM-033 - Keep primary form actions enabled

Keep primary form actions such as Add or Save enabled by default. Only disable them temporarily when an action is already processing, loading or otherwise cannot safely be repeated; use validation and clear feedback to handle incomplete or invalid input.

### IX-BASIC-FORM-034 - Make Back and Cancel behave consistently

When Back and Cancel both leave a form with unsaved changes, they should follow the same exit behaviour and preservation rules. If leaving would discard changes, use the same confirmation or recovery treatment for both.

### IX-BASIC-FORM-035 - Separate destructive footer actions

Place destructive actions such as Delete separately on the far left of the form footer, away from the standard Cancel and submit action group on the right. This separation reduces accidental activation and makes the difference in consequence immediately clear. For example Delete ← space → Cancel | Save

### IX-BASIC-FORM-036 - Match form presentation to complexity

Present low-complexity forms in dialogs, medium-complexity forms in drawers, and high-complexity forms on full pages so the available space, focus and navigation reflect the amount of information and interaction required.

### IX-BASIC-FORM-037 - Match form layout to complexity

Use a single-column layout for low-complexity dialog forms and medium-complexity drawer forms. High-complexity full-page forms may use a single reading path layout where this improves structure and scannability.

### IX-BASIC-FORM-038 - Use progressive form layouts in chat

Forms presented in chat must always use a single-column layout. Longer forms should behave like a wizard, surfacing one section at a time on demand to reduce cognitive load and guide users through completion.

### IX-BASIC-FORM-039 - Let users focus on mandatory fields

For complex forms, it is recommended to provide a header toggle labelled “Mandatory fields only” that hides optional fields, reduces distractions and lets users focus on the information required to complete the form more efficiently.

### IX-BASIC-FORM-040 - Support repetitive form entry

For forms that users may submit repeatedly, provide a footer option labelled “Add another”. When selected, this clears the form after submission so it is immediately ready for the next entry, reducing repeated navigation and effort.

### IX-BASIC-FORM-041 - Place destructive actions in edit views

Make permanent deletion available from a record’s edit screen rather than the main records list. This reduces accidental deletion and keeps destructive actions contextual. However, soft-delete actions, such as archive or deactivate, may be available from list views.

### IX-BASIC-FORM-042 - Use a danger zone for high-risk actions

Group highly destructive or irreversible actions in a clearly separated danger zone, away from routine settings. For additional protection, require administrators to enter their password or a confirmation keyword before the action can proceed.

### IX-BASIC-FORM-043 - Always confirm destructive deletions

Require users to explicitly confirm before permanently deleting a record. Clearly identify what will be deleted and the consequences of the action so users can verify their intent before proceeding.

---

## 07. Icons and iconography

### IX-BASIC-ICON-001 - Use Phosphor icons consistently

Use Phosphor icons throughout the interface. Use Regular by default, Fill for active, selected or emphasised states, and Duotone for shell or navigation elements where state is not conveyed. Avoid mixing icon libraries or inconsistent styles.

### IX-BASIC-ICON-002 - Optically align icons

Align icons by eye when geometric centring appears visually unbalanced. Small adjustments (using utility classes) can improve perceived alignment, especially when icon shapes have uneven visual weight or asymmetrical forms.

### IX-BASIC-ICON-003 - Use filled icons for active states

Use outline icons for default or inactive states and filled icons for active or selected states. This creates a clear visual distinction between states while keeping icon behaviour consistent and easy to recognise.

### IX-BASIC-ICON-004 - Animate icon state changes smoothly

Use a subtle cross-fade when icons change state, combining opacity, scale and blur to create a smooth transition. Keep motion brief and restrained so it provides clear feedback without distracting from the user’s task.

### IX-BASIC-ICON-005 - Use icons consistently for like actions

Always use the same icon for the same action throughout the product, and do not reuse that icon for a different meaning or context. A one-to-one relationship between icons and actions strengthens recognition, reduces ambiguity and lowers cognitive load.

---

## 08. Interaction and motion

### IX-BASIC-INTERACT-001 - Match enter and exit animations

Use matching enter and exit animations for the same surface or component. Mirrored motion helps interactions feel connected, reinforces where elements come from and go to, and creates more coherent transitions.

### IX-BASIC-INTERACT-002 - Use appropriate pointer cursors

Change the mouse cursor to reflect the type of interaction available. Use a hand cursor for links and other clickable elements, and apply the appropriate cursor for controls such as resizing, dragging or text selection.

### IX-BASIC-INTERACT-003 - Keep animation purposeful

Use animation to communicate changes in state, hierarchy or spatial relationships rather than as decoration. Motion should help users understand what happened without slowing progress or distracting from the task.

---

## 09. Layout and responsive design

### IX-BASIC-LAYOUT-001 - Use a standard content width

Keep pages to a consistent standard width to create predictable layouts, improve readability and maintain visual alignment across product. Consistent widths also reduce unnecessary variation and make interfaces more cohesive.

### IX-BASIC-LAYOUT-002 - Use concentric border radii

Use concentric border radii when nesting to create balanced, visually aligned corners. Set the nested element’s radius to the parent radius minus its padding so the inner and outer curves follow the same centre point.

### IX-BASIC-LAYOUT-003 - Use spacing to create hierarchy

Use whitespace intentionally to group related content, separate distinct sections and establish visual hierarchy before adding borders, containers or colour. Use tighter spacing to show relationships and greater spacing to signal separation.

### IX-BASIC-LAYOUT-004 - Use shadows to communicate depth

Use shadows to show elevation and visual depth between overlapping surfaces. Apply them consistently to help users understand which elements sit above others without introducing unnecessary decoration or visual noise.

### IX-BASIC-LAYOUT-005 - Use borders to define structure

Use borders to define boundaries, separate adjacent elements and reinforce interface structure where spacing alone is insufficient. Keep borders subtle and consistent, so they clarify relationships without adding unnecessary visual weight or competing with the content.

### IX-BASIC-LAYOUT-006 - Space nearby controls consistently

Leave 8px between adjacent controls to prevent accidental interaction and improve visual clarity. Consistent spacing helps users distinguish separate actions, supports touch accuracy and keeps control groups easier to scan.

### IX-BASIC-LAYOUT-007 - Prioritise content on smaller screens

On responsive layouts, preserve the most important content and actions first. Hide, collapse or move lower-priority information rather than shrinking everything until text, controls and interactions become difficult to read or use.

### IX-BASIC-LAYOUT-008 - Don’t rely on fixed heights for content

Allow containers to grow with their content unless a constrained height serves a clear interaction purpose. Fixed heights can cause clipping, unnecessary scrolling and layout problems when content or text size changes.

### IX-BASIC-LAYOUT-009 - Avoid unnecessary layout shifts

Reserve appropriate space for content that loads asynchronously so surrounding elements do not move unexpectedly. Stable layouts reduce accidental interaction, preserve reading position, improve visual comfort and make the interface feel more predictable while content is loading.

### IX-BASIC-LAYOUT-010 - Use consistent spacing increments

Use spacing values from the design system rather than arbitrary measurements. Consistent increments create stronger visual rhythm, make related content easier to recognise and reduce small layout inconsistencies.

### IX-BASIC-LAYOUT-011 - Align content to a shared grid

Align related content, controls and containers to shared grid lines. Consistent alignment strengthens visual relationships, improves scannability, supports predictable responsive behaviour and makes layouts feel intentionally composed.

### IX-BASIC-LAYOUT-012 - Avoid unnecessary nested cards

Don’t place cards inside cards unless the nested container represents a genuinely distinct grouping or hierarchy. Excessive nesting adds visual noise and can make relationships between content harder to understand.

### IX-BASIC-LAYOUT-013 - Use default component sizes

Use the default size of components wherever possible to maintain consistency across the interface. Only use smaller variants when space is genuinely constrained, or larger variants when additional emphasis or prominence is intentionally required.

---

## 10. Navigation and disclosure

### IX-BASIC-NAV-001 - Separate tabs from cards

Place tabs directly on the page background to clearly distinguish them from page content. Keeping tabs outside cards reinforces hierarchy, avoids implying they belong to a single content container and supports consistent layouts.

### IX-BASIC-NAV-002 - Use tabs for related views

Use tabs instead of button groups when switching between related views. Button groups serve a different purpose, such as triggering actions or selecting options. Tabs clarify relationships and provide familiar navigation.

### IX-BASIC-NAV-003 - Avoid dead ends in user journeys

Always provide a clear way forward when users reach the end of a task or encounter a blocked state. Use relevant guidance, navigation or actions to help them understand what has happened and what they can do next.

### IX-BASIC-NAV-004 - Make accordions open independently

Let users expand and collapse each accordion independently, including keeping multiple sections open at once. Don’t hide critical information inside collapsed sections, as important content should remain visible or clearly accessible without requiring discovery.

### IX-BASIC-NAV-005 - Limit the number of tabs

Use no more than eight tabs within a tab set. Too many tabs can become difficult to scan and navigate, particularly on smaller screens. If more sections are needed, consider adding an overflow or using an alternate approach.

### IX-BASIC-NAV-006 - Make tabs swipeable on mobile

Allow users to swipe horizontally through tab sets on touch devices when tabs exceed the available width. Keep the active tab visible and provide clear visual cues that additional tabs are available off-screen.

### IX-BASIC-NAV-007 - Limit items in an icon-only Sidebar

Limit each section of an icon-only Sidebar to eight items. Keeping navigation concise improves scannability and reduces cognitive load. If additional destinations are required, place lower-priority items in an overflow menu rather than extending the section.

### IX-BASIC-NAV-008 - Keep navigation labels concise

Use short, descriptive navigation labels that clearly communicate each destination. Avoid unnecessary words, jargon and vague terms so users can scan options quickly, distinguish destinations reliably and understand where each navigation item is likely to take them.

### IX-BASIC-NAV-009 - Show the current navigation location

Clearly indicate the user’s current location within navigation. Make the active state distinguishable through more than colour alone, using treatments such as weight, contrast, icons or supporting text so the current destination remains clear and accessible.

### IX-BASIC-NAV-010 - Use breadcrumbs for deep hierarchies

Use breadcrumbs when users navigate through multiple hierarchical levels and may need to return to a parent location. Avoid them for shallow structures where they add visual noise without improving orientation.

### IX-BASIC-NAV-011 - Avoid making entire cards clickable

Only make a whole card interactive when it has one clear destination or action. When cards contain multiple controls or links, keep interaction targets separate to avoid ambiguity, accidental activation and unclear keyboard navigation.

### IX-BASIC-NAV-012 - Use progressive disclosure

Show the information and controls most users need first, then reveal advanced or infrequently used options on request. This reduces cognitive load, keeps common tasks focused and preserves access to complexity without overwhelming the initial interface.

---

## 11. Tables and data

### IX-BASIC-TABLE-001 - Contain tables within a card

Place tables inside a card to group related data, establish clear visual boundaries and distinguish tabular content from the surrounding page. This reinforces hierarchy and helps keep layouts structured and consistent.

### IX-BASIC-TABLE-002 - Group table controls with the data

Place search inputs and filters within the table header to keep related controls close to the data they affect. This reinforces their relationship, makes them easier to find and use, and maintains a clear, consistent structure.

### IX-BASIC-TABLE-003 - Use full-width table rows

Extend table rows across the full width of their containing card. This creates a cleaner relationship between table and container, improves visual alignment, uses available space effectively and makes dense tabular content easier to scan.

### IX-BASIC-TABLE-004 - Use consistent table pagination

Include pagination in table footers, with Rows per page aligned left and Page X of X with Previous and Next controls aligned right. This creates a predictable pattern and helps users understand and navigate larger datasets.

### IX-BASIC-TABLE-005 - Use the first column for row selection

Where table row selection is required, use the first column for selection controls. Use radio buttons for single selection and checkboxes for multiple selection to provide a clear, consistent and accessible selection pattern.

### IX-BASIC-TABLE-006 - Use radio buttons for row single-select

Where only one table row can be selected, use radio buttons and allow only one selection across the entire table, including paginated pages. Selecting a different row must automatically deselect the previous row to keep selection behaviour clear and predictable.

### IX-BASIC-TABLE-007 - Use checkboxes for row multi-select

Where multiple rows can be selected, use checkboxes to support selection across paginated pages. Retain selections as users move between pages until they perform an action or explicitly clear the selection, keeping bulk selection predictable and persistent.

### IX-BASIC-TABLE-008 - Limit Select All to the current page

Apply Select All only to the table rows visible on the current page. This keeps table selection predictable, makes the scope of bulk actions clear and reduces the risk of users unintentionally affecting records they cannot see.

### IX-BASIC-TABLE-009 - Keep column headers free of inputs

Reserve column headers for labels and sorting controls. Avoid placing inputs or other interactive components within them, except for a Select All checkbox in a multi-select column. This keeps table structure clear and predictable.

### IX-BASIC-TABLE-010 - Place table actions in the last column

Place row-level actions in the final table column to create a consistent, predictable location. This makes actions easier to find when scanning rows and keeps the rest of the table focused on data.

### IX-BASIC-TABLE-011 - Use icon-only buttons for table actions

Use icon-only ghost buttons for common row-level table actions to keep the interface compact and reduce visual clutter. Only use familiar, unambiguous icons and provide accessible labels or tooltips where needed.

### IX-BASIC-TABLE-012 - Use multi-select for batch actions

Use multi-select only when users can perform the same action on multiple rows at once. For actions that apply to a single row, such as editing or viewing details, use individual row actions instead to keep selection purposeful and clear.

### IX-BASIC-TABLE-013 - Underline links in tables

Underline links within tables so users can distinguish interactive text from surrounding data. This improves discoverability and accessibility, especially in dense tables where colour alone may be insufficient to identify content that can be opened or followed.

### IX-BASIC-TABLE-014 - Use DD/MM/YYYY for table dates

Display dates in tables using the DD/MM/YYYY format to keep them consistent, predictable and easy to scan. Using a single date format also reduces ambiguity and maintains alignment across the product.

### IX-BASIC-TABLE-015 - Align table content consistently

Left-align table cell content by default and right-align numerical values, such as amounts, totals and percentages. Consistent alignment improves scannability, makes values easier to compare and helps users interpret tabular information more efficiently.

### IX-BASIC-TABLE-016 - Use badges sparingly for status or priority

Use badges sparingly, and only to highlight status or priority where quick recognition matters. Avoid using badges for general metadata or decorative emphasis, and when both status and priority are shown together, use a badge for status and plain text for priority.

### IX-BASIC-TABLE-017 - Keep table badges icon-free

Avoid icons within table badges unless an icon communicates information that the text cannot provide alone. In dense tables, unnecessary icons increase visual noise, reduce readability and make multiple status or priority badges harder to scan.

### IX-BASIC-TABLE-018 - Use soft colours for table badges

Use soft colours for badges in tables to reduce visual weight and prevent status information from dominating the layout. This keeps dense tables easier to scan while still allowing important states or priorities to stand out.

### IX-BASIC-TABLE-019 - Use Previous and Next for pagination

Use Previous and Next as the default pagination controls instead of numbered pages. This keeps table navigation simple, predictable and consistent, while reducing unnecessary visual complexity in the table footer.

### IX-BASIC-TABLE-020 - Place status before row actions

Place the Status column immediately before row actions so records naturally flow from identifying information to current state and available actions. If status is a primary way users scan or triage the table, position it further left instead.

### IX-BASIC-TABLE-021 - Place priority next to status

Keep Priority and Status columns together, as they provide closely related information about a record’s current state and importance. Grouping them improves scannability, supports faster comparison and makes operational tables easier to understand at a glance.

### IX-BASIC-TABLE-022 - Don’t clear filters unexpectedly

Preserve applied filters, sorting and search terms when users navigate into a record and return to a table. Maintaining state prevents users from recreating their previous view and helps them continue where they left off.

### IX-BASIC-TABLE-023 - Make applied filters visible

Clearly show which filters are active so users understand why they are seeing particular results. Provide simple controls to remove individual filters or clear all filters and return to the unfiltered view.

### IX-BASIC-TABLE-024 - Show the number of active filters

When filter controls are collapsed or hidden, show how many filters are active. This makes restricted results easier to understand and reminds users that filtering still applies even when the controls themselves are not currently visible.

### IX-BASIC-TABLE-025 - Keep table headers visible

Keep column headers visible while users scroll through long tables. Persistent headers preserve context, make values easier to interpret further down the dataset and reduce the need to repeatedly return to the top to identify each column.

### IX-BASIC-TABLE-026 - Avoid horizontal table scrolling

Design tables and layouts to fit the available viewport without relying on horizontal scrolling. Prioritise responsive layouts that reflow content, stack columns or reveal secondary information progressively so users can access everything without scrolling sideways.

### IX-BASIC-TABLE-027 - Keep comparable data in consistent columns

Place the same type of information in the same column across every row. Consistent column structure makes tables easier to scan, compare and understand, and prevents users from having to reinterpret the meaning or position of data between records.

### IX-BASIC-TABLE-028 - Prioritise important columns

Place the most important identifying and decision-making information towards the left of the table, where users typically begin scanning. Move supporting or lower-priority information further right so essential data remains easier to find and compare.

### IX-BASIC-TABLE-029 - Limit visible table columns

Show only the columns users need for their primary task and avoid exposing excessive secondary information by default. Prioritise essential data and progressively reveal additional details where needed to keep tables manageable, readable and easier to scan.

### IX-BASIC-TABLE-030 - Keep table columns consistent

Use the same column names, terminology and relative order for equivalent data across different tables and pages. Consistency reduces relearning, improves scanability and helps users build reliable expectations when moving between related views.

### IX-BASIC-TABLE-031 - Size tables to data complexity

Use a maximum width of 1024px for smaller, less data-heavy tables. Use the full available page width for more complex tables with additional columns, longer values or greater need for side-by-side comparison.

### IX-BASIC-TABLE-032 - Adapt tables for mobile

On mobile, simplify complex tables by changing their structure where needed. Hide or progressively disclose secondary columns, or use an alternative layout such as stacked cards when a conventional table would be difficult to scan or use.

### IX-BASIC-TABLE-033 - Wrap column headers

Wrap column header text onto multiple lines when it is wider than the available column width. Do not truncate headers, as users need the full label to understand the data and distinguish between similar columns.

### IX-BASIC-TABLE-034 - Keep column headers concise

Use short, descriptive column header labels, ideally one or two words. Avoid unnecessary wording so headers are easy to scan, require less space and reduce the likelihood of wrapping.

### IX-BASIC-TABLE-035 - Limit row actions

Show no more than two actions directly within each table row. If additional actions are required, use a single overflow button and place the remaining actions in a dropdown menu.

### IX-BASIC-TABLE-036 - Add new entries first

Add newly created table entries to the top of the list so they are immediately visible after creation. This helps users confirm that their action was successful without needing to search, sort or navigate through the table.

### IX-BASIC-TABLE-037 - Size columns appropriately

Size table columns according to the expected length and type of their content. Give longer values sufficient space while keeping short or predictable values compact, helping the table remain readable, balanced and easy to scan.

### IX-BASIC-TABLE-038 - Use zebra striping

Use alternating row backgrounds in data-heavy tables to help users visually track content across rows. Ensure the contrast between alternating rows is subtle but distinguishable and does not reduce text or control accessibility.

### IX-BASIC-TABLE-039 - Hide controls for empty tables

When a table contains no data on first load, hide search, filters and pagination controls until entries are available. This avoids presenting controls that cannot perform a useful action and keeps the empty state focused.

### IX-BASIC-TABLE-040 - Label cells with no data

Use explicit text such as “N/A” or “No data” when a table cell has no value. Do not leave cells blank, as screen reader users may be unable to distinguish between missing data, a zero value or a rendering error.

### IX-BASIC-TABLE-041 - Avoid ambiguous row action icons

Use familiar, recognised icons for common row actions, such as a pencil for edit and a bin for delete. Avoid unconventional or ambiguous icons, and always provide accessible labels or tooltips so each action is clearly understood.

### IX-BASIC-TABLE-042 - Show units in column headers

Show measurement units in the column header when every value uses the same unit, rather than repeating them in each cell, e.g. “£”. This reduces visual noise, saves space and makes numerical data easier to scan and compare.

### IX-BASIC-TABLE-043 - Hide unnecessary pagination

Hide pagination controls, including rows per page and previous or next buttons, when all table rows fit on a single page. Only show pagination when users can meaningfully navigate between multiple pages of data.

### IX-BASIC-TABLE-044 - Top-align multi-line rows

When content in any table cell wraps onto multiple lines, align the content in all cells within that row to the top. This keeps related values visually aligned and makes longer rows easier to scan and understand.

### IX-BASIC-TABLE-045 - Keep priority and status distinct

Do not use priority and status interchangeably. Priority indicates how important or urgent an item is, while status describes its current state or progress. Treat them as separate attributes with distinct labels, values and visual treatments.

### IX-BASIC-TABLE-046 - Use inline editing for simple values

Allow simple, frequently changed table values, such as status or assignment, to be edited directly within the cell. Use appropriate controls and provide clear feedback so users can make quick changes without opening a separate page or dialog.

### IX-BASIC-TABLE-047 - Freeze the first column on mobile

When a table must scroll horizontally on mobile, keep the first column fixed so users retain the row context while viewing additional columns. Ensure the frozen column remains clearly separated from scrolling content and does not obscure important data.

### IX-BASIC-TABLE-048 - Prefer infinite scrolling on mobile

Use infinite scrolling for long lists on mobile where users are primarily browsing content sequentially. It provides a more natural, continuous touch experience than pagination controls, but preserve position and provide clear loading and end-of-list feedback.

### IX-BASIC-TABLE-049 - Avoid conflicting row links

Do not make an entire table row selectable when individual cells already contain links or other interactive controls. Multiple overlapping link targets create ambiguous interaction behaviour, can cause accessibility issues and are semantically incorrect.
