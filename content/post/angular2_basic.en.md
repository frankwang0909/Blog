+++
categories = ["frontend"]
tags = ["Angular 2"]
date = "2017-07-15T17:13:18+08:00"
title = "Angular 2 Basics"
keywords = ["Angular 2", "components", "template", "metadata", "data binding", "directive", "service", "dependency injection", "module"]
description = "A practical introduction to Angular 2 core concepts: components, templates, metadata, data binding, directives, services, dependency injection, and modules."
url = "/angular2_basic.html"
+++

![](/images/2017071501.jpg)

## 1. Components

![](/images/2017071502.jpg)

### 1.1 Components and Example Code
```typescript
// Decorator
@Component({
    // metadata

    selector: 'hello',

    // Define the component's template
    template: '<p>{{greeting}}</p>
})

// Component class
export class HelloComponent {
    private greeting: string;
    constructor() {
        this.greeting = 'Hello, Welcome to Angular 2!';
    }
}
```

![](/images/2017071505.jpg)

1. Decorator: `@Component`

Decorators attach metadata to a class so Angular knows how to treat it as a component.

2. Metadata

Metadata describes configuration such as the selector, template, and dependencies.

3. Template

You can define an inline template in metadata, or reference an external template file with `templateUrl`.

4. Data binding:

1) Interpolation: `{{variableName}}` for rendering component data in templates.

2) Property binding: `[prop]=\"value\"` to pass data from a component class to its template (or to a child component input).
```typescript
     <input [message]="myData" />
```

3) Event binding: `(event)=\"handler($event)\"` to pass user interactions from the template back to the component class.
```typescript
    <input (keyup)="handle($event)" />
```

4) Two-way binding: `[(ngModel)]` for synchronized updates between template state and component state.
```typescript
    <input [(ngModel)]="myData" />
```

### 1.2 Component tree

![](/images/2017071506.jpg)

### 1.3 Component Communication and Data Flow

![](/images/2017071503.jpg)

![](/images/2017071507.jpg)

### 1.4 Component Lifecycle and Hooks

![](/images/2017071504.jpg)

1. `constructor`: initialize fields and inject dependencies.

2. `OnChanges`: runs when input properties change, including the first binding.

3. `OnInit`: runs once after the first `OnChanges`; good for startup logic.

4. `DoCheck` / change detection: runs during change detection cycles.

5. `OnDestroy`: cleanup phase (unsubscribe, detach handlers, release resources).


## 2. Directives

A component is a directive with its own template.

### 2.1 Attribute Directives

Attribute directives change the appearance or behavior of existing elements (for example, styles).


### 2.2 Structural Directives

Structural directives change DOM layout, for example `*ngIf` inserts or removes nodes.


### 2.3 Custom Directives
```typescript
// Custom directive highlight
// Import Directive, ElementRef, and Renderer to control element rendering.
import { Directive, ElementRef, Renderer } from '@angular/core';

@Directive({
    selector: "[highlight]" // Square brackets indicate that the directive is used on element attributes
})

export class HighlightDirective {
    constructor(private el: ElementRef, private renderer:Renderer) { 
        renderer.setElementStyle(el.nativeElement, 'backgroundColor', 'pink');
    }
}
```

## 3. Services

A service is a class that encapsulates reusable business logic, such as logging.
```typescript
export class LoggerService {
    constructor() {}

    debug(msg: string) {
        console.log(msg);
    }

    error(msg: string) {
        console.error(msg);
    }
}
```

## 4. Dependency Injection

### 4.1 Dependency Injection

Dependency injection (DI) is the mechanism Angular uses to provide dependencies (such as services) to components and other classes. In practice, Angular creates service instances and stores them in injectors so they can be reused.

![](/images/2017071508.jpg)

Example:
```typescript
@Component({
    selector: 'hello',
    template: '<p>{{greeting}}</p>
    
    // Dependency injection configuration
    providers:[LoggerService]
})

export class HelloComponent {
    private greeting: string;

    // Constructor injection: Angular resolves LoggerService from the injector
    constructor(logger: LoggerService){
        this.greeting = 'Hello, Angular 2';
        logger.debug('Constructor complete');
    }
}
```

### 4.2 Hierarchical Dependency Injection

Services provided in a parent scope can be consumed by that component and its children.

![](/images/2017071509.jpg)

## 5. Modules

### 5.1 File-Level Modules

1. Common framework modules:

1) Core module: @angular/core

2) Common module: @angular/common

3) Form module: @angular/forms

4) Network module: @angular/http

5) Other modules

2. Using modules:

Before using a framework module, import it explicitly:
```typescript
import { Http } from "@angular/http";

import { Component } from "@angular/core";

import { Directive } from "@angular/core";

import { ElementRef, Renderer } from "@angular/core";
```

### 5.2 Application Modules

![](/images/2017071510.jpg)

1. Group related components, services, and directives into feature modules by responsibility.

2. Module interaction:

By default, components can only use declarations that are visible in their module context. To use declarations from another module, import that module.
```typescript
// @NgModule declares the module
@NgModule({

    // Wrap components or directives
    declarations: [
        AppComponent,
        HelloComponent,
        SomeDirective
    ],

    // Dependency injection service
    providers: [ LoggerService ],

    // Import other modules
    imports: [OtherModule ],

    // Set root component
    bootstrap: [ AppComponent],

    // Export the directives or modules exposed by this module for calls by other components
    exports:[ SomeDirective ]
})

export class AppModule {}
```

After importing another module, you can use its exported components/directives and services provided through DI.

3. Root, feature, shared, and core modules

An Angular app is usually split by responsibility:
- `root module` as the app entry point
- `feature modules` for domain-specific functionality
- `shared modules` for reusable UI building blocks
- `core modules` for app-wide singleton services and infrastructure

![](/images/20170715011.jpg)
